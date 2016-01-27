# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rs_settings.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(330, 267)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.cb_baud = QtGui.QComboBox(Dialog)
        self.cb_baud.setObjectName(_fromUtf8("cb_baud"))
        self.gridLayout.addWidget(self.cb_baud, 1, 1, 1, 1)
        self.l_port = QtGui.QLabel(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_port.sizePolicy().hasHeightForWidth())
        self.l_port.setSizePolicy(sizePolicy)
        self.l_port.setObjectName(_fromUtf8("l_port"))
        self.gridLayout.addWidget(self.l_port, 0, 0, 1, 1)
        self.l_parity = QtGui.QLabel(Dialog)
        self.l_parity.setObjectName(_fromUtf8("l_parity"))
        self.gridLayout.addWidget(self.l_parity, 2, 0, 1, 1)
        self.l_baud = QtGui.QLabel(Dialog)
        self.l_baud.setObjectName(_fromUtf8("l_baud"))
        self.gridLayout.addWidget(self.l_baud, 1, 0, 1, 1)
        self.cb_port = QtGui.QComboBox(Dialog)
        self.cb_port.setObjectName(_fromUtf8("cb_port"))
        self.gridLayout.addWidget(self.cb_port, 0, 1, 1, 1)
        self.cb_db = QtGui.QComboBox(Dialog)
        self.cb_db.setObjectName(_fromUtf8("cb_db"))
        self.gridLayout.addWidget(self.cb_db, 3, 1, 1, 1)
        self.l_sb = QtGui.QLabel(Dialog)
        self.l_sb.setObjectName(_fromUtf8("l_sb"))
        self.gridLayout.addWidget(self.l_sb, 4, 0, 1, 1)
        self.l_db = QtGui.QLabel(Dialog)
        self.l_db.setObjectName(_fromUtf8("l_db"))
        self.gridLayout.addWidget(self.l_db, 3, 0, 1, 1)
        self.cb_sb = QtGui.QComboBox(Dialog)
        self.cb_sb.setObjectName(_fromUtf8("cb_sb"))
        self.gridLayout.addWidget(self.cb_sb, 4, 1, 1, 1)
        self.cb_parity = QtGui.QComboBox(Dialog)
        self.cb_parity.setObjectName(_fromUtf8("cb_parity"))
        self.gridLayout.addWidget(self.cb_parity, 2, 1, 1, 1)
        self.frame = QtGui.QFrame(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pb_accept = QtGui.QPushButton(self.frame)
        self.pb_accept.setObjectName(_fromUtf8("pb_accept"))
        self.horizontalLayout.addWidget(self.pb_accept)
        self.pb_cancel = QtGui.QPushButton(self.frame)
        self.pb_cancel.setObjectName(_fromUtf8("pb_cancel"))
        self.horizontalLayout.addWidget(self.pb_cancel)
        self.gridLayout.addWidget(self.frame, 5, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.l_port.setText(_translate("Dialog", "Port:", None))
        self.l_parity.setText(_translate("Dialog", "Parity:", None))
        self.l_baud.setText(_translate("Dialog", "Baudrate:", None))
        self.l_sb.setText(_translate("Dialog", "Stop bits:", None))
        self.l_db.setText(_translate("Dialog", "Data bits:", None))
        self.pb_accept.setText(_translate("Dialog", "Accept", None))
        self.pb_cancel.setText(_translate("Dialog", "Cancel", None))

