import sys
from time import strftime,sleep


import serial
from PyQt4 import QtGui,Qt
from PyQt4.QtCore import pyqtSignal,QObject,QThread

from dialog.rs_settings import rs_settings
from gui.main_window_test import Ui_MainWindow
from utilities.serial_rcv_thread import rcv_thread
from widgets.connectionBar import connectionBar
from widgets.manual_control import manual_control
from widgets.positionList import positionlist
from widgets.editor import editor



class main_window(QtGui.QMainWindow):
    closing = pyqtSignal()
    updatePositionList=pyqtSignal()
    positionSaved=pyqtSignal()

    def __init__(self,port):
        super(main_window,self).__init__()

        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.connBar=connectionBar()
        self.ui.toolBar.addWidget(self.connBar)

        self.port=port

        self.rs_dialog=rs_settings(self.port,parent=self)
        self.rcv_thread=rcv_thread(self.port)

        self.set_signals()
        self.set_mdi()

        self.list_of_positions=[]
        self.reader=Reader()
        self.reader.end.connect(self.readingEnded)
        # self.reader_thread=QThread()
        # self.reader.moveToThread(self.reader_thread)
        self.reader.save.connect(self.addPosition)
        self.pos_nr=1;
        self.catch=False

    def set_signals(self):
        self.ui.actionSerial_port.triggered.connect(self.serial_clicked)
        self.ui.actionExit.triggered.connect(self.close)

        self.rs_dialog.rs_data_sig.connect(self.update_port_settings)

        self.ui.pb_connect.clicked.connect(self.open_serial)
        self.ui.actionConnect.triggered.connect(self.open_serial)

        self.ui.pb_disconnect.clicked.connect(self.close_serial)
        self.ui.actionDisconnect.triggered.connect(self.close_serial)

        self.rcv_thread.rcv_data.connect(self.data_received)

        self.ui.pb_send.clicked.connect(self.data_send)
        self.ui.en_send.returnPressed.connect(self.data_send)

        self.ui.pb_clear.clicked.connect(self.clear_list)

        self.ui.pb_manualControl.clicked.connect(self.manualControll_toggle)
        self.ui.actionManual_control.triggered.connect(self.manualControll_toggle)

        self.ui.pb_postionList.clicked.connect(self.positionList_toggle)
        self.ui.actionPosition_list.triggered.connect(self.positionList_toggle)

        self.ui.pb_editor.clicked.connect(self.editor_toggle)
        self.ui.actionEditor.triggered.connect(self.editor_toggle)

    def set_mdi(self):
        self.manCon_isOpen=False
        self.IO_isOPen=False
        self.editor_isOpen=False
        self.posList_isOPen=False

    def closeEvent(self, event):
        self.closing.emit()

    def serial_clicked(self):
        self.rs_dialog.show()

    def update_port_settings(self,data,port_name):
        self.port.apply_settings(data)
        self.port.port=port_name
        self.connBar.updateParameters(port_name,"{},{},{},{}".format(
            str(data["baudrate"]),str(data["parity"]),str(data["bytesize"]),str(data["stopbits"])))

    def open_serial(self):
        if not self.port.isOpen():
            try:
                self.port.open()
                self.connBar.updateStatus("Connected")
                self.rcv_thread.isAlive=True
                self.rcv_thread.start()
            except Exception as e:
                self.connBar.updateStatus(str(e))
            self.update_ui()

    def close_serial(self):

        if self.port.isOpen():
            self.rcv_thread.isAlive=False
            self.rcv_thread.wait(1)
            self.reader.wait(1)
            for window in self.ui.mdiArea.subWindowList():
                window.close()
            self.port.close()
            self.connBar.updateStatus("Disconnected")
            self.update_ui()

    def update_ui(self):
        self.ui.pb_connect.setEnabled(not self.port.isOpen())
        self.ui.pb_disconnect.setEnabled(self.port.isOpen())
        # self.ui.pb_IOconsole.setEnabled(self.port.isOpen())
        self.ui.pb_manualControl.setEnabled(self.port.isOpen())
        self.ui.pb_editor.setEnabled(self.port.isOpen())
        self.ui.pb_postionList.setEnabled(self.port.isOpen())

        self.ui.actionConnect.setEnabled(not self.port.isOpen())
        self.ui.actionDisconnect.setEnabled(self.port.isOpen())
        # self.ui.actionI_O_console.setEnabled(self.port.isOpen())
        self.ui.actionManual_control.setEnabled(self.port.isOpen())
        self.ui.actionEditor.setEnabled(self.port.isOpen())
        self.ui.actionPosition_list.setEnabled(self.port.isOpen())

        self.ui.gb_communication.setEnabled(self.port.isOpen())

        self.ui.actionSerial_port.setEnabled(not self.port.isOpen())

    def update_list(self,string,style):
        item=QtGui.QListWidgetItem()
        item.setText(string)
        item.setForeground(Qt.QColor(style))
        self.ui.lw_received.addItem(item)
        self.ui.lw_received.scrollToBottom()

    def clear_list(self):
        self.ui.lw_received.clear()

    def data_received(self,string,):
        string=string.replace("\n","")
        self.update_list('{} << {}'.format(strftime("%H:%M:%S"),string),"#FF0A0A")
        if self.catch:
            self.list_of_positions.append("{};{}".format(self.pos_nr,string))
            print("lenght:{}".format(len(self.list_of_positions)))
            self.reader.waitForPos=False
            self.catch=False
            self.updatePositionList.emit()

    def send_rs(self,string):
       if string!=None and string!="":
            data="{}\r".format(string)
            self.update_list("{} >> {}".format(strftime("%H:%M:%S"),data),"#0AA00A")
            self.port.write(bytes(data,"UTF-8"))

    def refreshTable(self):
        if not self.reader.isRunning():
            self.positionList_widget.ui.actionRefresh.setEnabled(False)
            del self.list_of_positions[:]
            self.updatePositionList.emit()
            self.reader.start()
        pass
    def data_send(self):
        data=self.ui.en_send.text()
        self.send_rs(data)
        self.ui.en_send.clear()
        self.ui.en_send.setFocus()

    def manualControll_toggle(self):
        try:
            self.manualControll_widget.setFocus()
        except:
            self.manCon_isOpen=False

        if not self.manCon_isOpen:
            self.manCon_isOpen=True
            self.manualControll_widget=manual_control()
            self.manualControll_widget.send.connect(self.send_rs)
            # self.manualControll_widget.position.connect(self.position_save)
            self.ui.mdiArea.addSubWindow(self.manualControll_widget)
            self.manualControll_widget.show()

    def positionList_toggle(self):
        try:
            self.positionList_widget.setFocus()
        except:
            self.posList_isOPen=False

        if not self.posList_isOPen:
            # self.refreshTable()
            self.positionList_widget=positionlist(self.list_of_positions,self)
            self.ui.mdiArea.addSubWindow(self.positionList_widget)
            self.positionList_widget.send_rs.connect(self.send_rs)
            self.positionList_widget.ui.actionRefresh.triggered.connect(self.refreshTable)
            self.positionList_widget.ui.actionCancel.triggered.connect(self.cancelRefresh)
            self.positionList_widget.show()
            self.posList_isOPen=True

    def editor_toggle(self):
        try:
            self.editor_widget.setFocus()
        except:
            self.editor_isOpen=False

        if not self.editor_isOpen:
            self.editor_widget=editor(self)
            self.ui.mdiArea.addSubWindow(self.editor_widget)
            self.editor_widget.send.connect(self.send_rs)
            self.editor_widget.program_sent.connect(self.update_list)
            self.editor_widget.show()
            self.editor_isOpen=True

    def addPosition(self,nr):
        self.pos_nr=nr
        self.catch=True
        self.send_rs("PR {}".format(nr))
        # self.send_rs("WH")

    def cancelRefresh(self):
        self.reader.cancel=True
        self.catch=False
        # self.reader.stop()
        self.updatePositionList.emit()
        # self.update_list("{} || Positions list refersh - abort".format(strftime("%H:%M:%S")),'#0A0AA0')
        # self.positionList_widget.ui.actionRefresh.setEnabled(True)

    def readingEnded(self):
        try:
            self.positionList_widget.ui.actionRefresh.setEnabled(True)
            self.update_list("{} || Reading positions ended".format(strftime("%H:%M:%S")),'#0A0AA0')
        except:
            pass




class Reader(QThread):
    save=pyqtSignal(int)
    end=pyqtSignal()
    def __init__(self):
        QThread.__init__(self)
        self.waitForPos=True
        self.cancel=False


    def run(self):
        for i in range(0,99):
            print(i+1)
            self.save.emit(i+1)
            while self.waitForPos:
                if self.cancel:
                    # self.cancel=False
                    break
                QThread.msleep(10)
                pass
            self.waitForPos=True
            if self.cancel:
                self.cancel=False
                break
        self.end.emit()





if __name__ == "__main__":
    port=serial.Serial()
    port.port="COM1"
    port.parity=serial.PARITY_EVEN
    port.stopbits=serial.STOPBITS_TWO
    # print (port.timeout)

    app = QtGui.QApplication(sys.argv)
    ex = main_window(port)
    # ex.show()
    ex.showMaximized()
    sys.exit(app.exec_())
