# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connectionStatus.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(341, 60)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gb_connection = QtGui.QFrame(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gb_connection.sizePolicy().hasHeightForWidth())
        self.gb_connection.setSizePolicy(sizePolicy)
        self.gb_connection.setMaximumSize(QtCore.QSize(16777215, 100))
        self.gb_connection.setObjectName(_fromUtf8("gb_connection"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.gb_connection)
        self.horizontalLayout.setContentsMargins(9, 3, 9, 4)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.l_connectionStatus = QtGui.QLabel(self.gb_connection)
        self.l_connectionStatus.setObjectName(_fromUtf8("l_connectionStatus"))
        self.horizontalLayout.addWidget(self.l_connectionStatus)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.line = QtGui.QFrame(self.gb_connection)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout.addWidget(self.line)
        self.l_portName = QtGui.QLabel(self.gb_connection)
        self.l_portName.setObjectName(_fromUtf8("l_portName"))
        self.horizontalLayout.addWidget(self.l_portName)
        self.line_2 = QtGui.QFrame(self.gb_connection)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.horizontalLayout.addWidget(self.line_2)
        self.l_portParameters = QtGui.QLabel(self.gb_connection)
        self.l_portParameters.setObjectName(_fromUtf8("l_portParameters"))
        self.horizontalLayout.addWidget(self.l_portParameters)
        self.verticalLayout.addWidget(self.gb_connection)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.l_connectionStatus.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Disconnected</span></p></body></html>", None))
        self.l_portName.setText(_translate("Form", "<html><head/><body><p>COM1</p></body></html>", None))
        self.l_portParameters.setText(_translate("Form", "<html><head/><body><p>9600,E,8,2</p></body></html>", None))

