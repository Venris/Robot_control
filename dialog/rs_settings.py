from gui.rs_settings import Ui_Dialog
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignal
import serial
import serial.tools.list_ports

class rs_settings(QDialog):
    rs_data_sig=pyqtSignal(dict,str)
    def __init__(self,port,parent=None):
        super(rs_settings,self).__init__()

        self.ui=Ui_Dialog()
        self.ui.setupUi(self)

        self.parent=parent

        self.port=port

        self.set_signals()

    def showEvent(self, QShowEvent):
        self.fill_combo_box()
        self.set_port_parameters()

    def fill_combo_box(self):
        # ports
        self.ui.cb_port.clear()
        port_list=(list(serial.tools.list_ports.comports()))
        for p in port_list:
            self.ui.cb_port.addItem(p[0])

        # baud rates
        self.ui.cb_baud.clear()
        baud_rate_list=serial.Serial.BAUDRATES
        for b in baud_rate_list:
            self.ui.cb_baud.addItem(str(b),b)

        # parities
        self.ui.cb_parity.clear()
        parity_list=serial.Serial.PARITIES
        for p in parity_list:
            self.ui.cb_parity.addItem(str(p),p)

        # stop bits
        self.ui.cb_sb.clear()
        stop_bits_list = serial.Serial.STOPBITS
        for sb in stop_bits_list:
            self.ui.cb_sb.addItem(str(sb),sb)

        # data bits
        self.ui.cb_db.clear()
        data_bits_list = serial.Serial.BYTESIZES
        for db in data_bits_list:
            self.ui.cb_db.addItem(str(db),db)


        pass

    def set_port_parameters(self):
        self.port_settings=self.port.getSettingsDict()

        self.ui.cb_port.setCurrentIndex(self.ui.cb_port.findText(self.port.port))
        self.ui.cb_parity.setCurrentIndex(self.ui.cb_parity.findText(str(self.port_settings["parity"])))
        self.ui.cb_baud.setCurrentIndex(self.ui.cb_baud.findText(str(self.port_settings["baudrate"])))
        self.ui.cb_sb.setCurrentIndex(self.ui.cb_sb.findText(str(self.port_settings["stopbits"])))
        self.ui.cb_db.setCurrentIndex(self.ui.cb_db.findText(str(self.port_settings["bytesize"])))


        pass

    def set_signals(self):
        self.ui.pb_accept.clicked.connect(self.accept_clicked)
        self.ui.pb_cancel.clicked.connect(self.cancel_clicked)

        self.parent.closing.connect(self.close)
        pass

    def accept_clicked(self):
        # print (type(db))
        self.port_settings={
            "baudrate": self.ui.cb_baud.itemData(self.ui.cb_baud.currentIndex()),
            "parity": self.ui.cb_parity.itemData(self.ui.cb_parity.currentIndex()),
            "stopbits": self.ui.cb_sb.itemData(self.ui.cb_sb.currentIndex()),
            "bytesize": self.ui.cb_db.itemData(self.ui.cb_db.currentIndex())
        }
        self.rs_data_sig.emit(self.port_settings,self.ui.cb_port.currentText())
        self.close()
        pass

    def cancel_clicked(self):
        self.close()
        pass


