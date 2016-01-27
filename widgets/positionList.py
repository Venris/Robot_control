from PyQt4 import QtGui
from PyQt4.QtCore import pyqtSignal,Qt, QThread
from gui.postionlist import Ui_MainWindow



class positionlist(QtGui.QMainWindow):
    send_rs=pyqtSignal(str)
    positionSave=pyqtSignal(int)
    positionClear=pyqtSignal()



    def __init__(self,list,parent):
        super(positionlist, self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.list=list
        self.ui.actionMove_to.triggered.connect(self.sendposition)
        parent.updatePositionList.connect(self.updateTable)

    def showEvent(self, QShowEvent):
        self.updateTable()

    def updateTable(self):
        print("dl:{}".format(len(self.list)))
        rows=self.ui.tableWidget.rowCount()
        for i in range(rows):
            self.ui.tableWidget.removeRow(0)

        for row in self.list:
            splitted=row.split(";")
            nr=splitted[0]
            tmp=splitted[1].split(",")
            position=",".join(tmp[0:3])
            orientation=",".join(tmp[3:])
            if position!="0,0,0" and orientation!="0,0,0":
                self.insertRow([nr,position,orientation])

            self.ui.tableWidget.scrollToBottom()



    def insertRow(self,data):
        currentRowCount = self.ui.tableWidget.rowCount() #necessary even when there are no rows in the table
        self.ui.tableWidget.insertRow(currentRowCount)

        for i,element in enumerate(data):
            item=QtGui.QTableWidgetItem("{}".format(str(element)))
            # item.setFlags(Qt.ItemIsEditable)
            self.ui.tableWidget.setItem(currentRowCount,i,item)

        self.ui.tableWidget.resizeColumnsToContents()

    def sendposition(self):
        try:
            row=self.ui.tableWidget.currentRow()
            widget=self.ui.tableWidget.item(row,0)
            msg=widget.text()
            self.send_rs.emit("MO {}".format(msg.rstrip()))
        except:
            pass
