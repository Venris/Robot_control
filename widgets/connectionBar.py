from  PyQt4 import QtGui
from gui.connectionStatus import Ui_Form

class connectionBar(QtGui.QWidget):
    def __init__(self):
        super(connectionBar, self).__init__()
        self.ui=Ui_Form()
        self.ui.setupUi(self)

        self.ui.l_portName.setStyleSheet("font-size: 8pt")
        self.ui.l_portParameters.setStyleSheet("font-size: 8pt")
        self.ui.l_connectionStatus.setStyleSheet(" font-size:10pt; font-weight:600;")
        pass

    def updateStatus(self,txt):
        self.ui.l_connectionStatus.setText(txt)

    def updateParameters(self,name,parameters):
        self.ui.l_portName.setText(name)
        self.ui.l_portParameters.setText(parameters)
