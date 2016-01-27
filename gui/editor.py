# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editor.ui'
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

class Ui_Editor_window(object):
    def setupUi(self, Editor_window):
        Editor_window.setObjectName(_fromUtf8("Editor_window"))
        Editor_window.resize(473, 379)
        self.centralwidget = QtGui.QWidget(Editor_window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.textEdit = QtGui.QPlainTextEdit(self.centralwidget)
        self.textEdit.setStyleSheet(_fromUtf8("font: 10pt \"MS Shell Dlg 2\";\n"
""))
        self.textEdit.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout.addWidget(self.textEdit)
        Editor_window.setCentralWidget(self.centralwidget)
        self.tb_files = QtGui.QToolBar(Editor_window)
        self.tb_files.setIconSize(QtCore.QSize(16, 16))
        self.tb_files.setObjectName(_fromUtf8("tb_files"))
        Editor_window.addToolBar(QtCore.Qt.TopToolBarArea, self.tb_files)
        self.tb_edit = QtGui.QToolBar(Editor_window)
        self.tb_edit.setIconSize(QtCore.QSize(16, 16))
        self.tb_edit.setObjectName(_fromUtf8("tb_edit"))
        Editor_window.addToolBar(QtCore.Qt.TopToolBarArea, self.tb_edit)
        self.tb_communication = QtGui.QToolBar(Editor_window)
        self.tb_communication.setIconSize(QtCore.QSize(16, 16))
        self.tb_communication.setObjectName(_fromUtf8("tb_communication"))
        Editor_window.addToolBar(QtCore.Qt.TopToolBarArea, self.tb_communication)
        self.actionOpen = QtGui.QAction(Editor_window)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/folder.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionSave = QtGui.QAction(Editor_window)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/bullet_disk.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon1)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionClear = QtGui.QAction(Editor_window)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/page_white.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClear.setIcon(icon2)
        self.actionClear.setObjectName(_fromUtf8("actionClear"))
        self.actionUpload = QtGui.QAction(Editor_window)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/application_get.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUpload.setIcon(icon3)
        self.actionUpload.setObjectName(_fromUtf8("actionUpload"))
        self.actionRun = QtGui.QAction(Editor_window)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/application_go.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRun.setIcon(icon4)
        self.actionRun.setObjectName(_fromUtf8("actionRun"))
        self.actionRedo = QtGui.QAction(Editor_window)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/arrow_redo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRedo.setIcon(icon5)
        self.actionRedo.setObjectName(_fromUtf8("actionRedo"))
        self.actionUndo = QtGui.QAction(Editor_window)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/arrow_undo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUndo.setIcon(icon6)
        self.actionUndo.setObjectName(_fromUtf8("actionUndo"))
        self.actionStop = QtGui.QAction(Editor_window)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStop.setIcon(icon7)
        self.actionStop.setObjectName(_fromUtf8("actionStop"))
        self.tb_files.addAction(self.actionOpen)
        self.tb_files.addAction(self.actionSave)
        self.tb_files.addSeparator()
        self.tb_edit.addAction(self.actionUndo)
        self.tb_edit.addAction(self.actionRedo)
        self.tb_edit.addAction(self.actionClear)
        self.tb_communication.addAction(self.actionUpload)
        self.tb_communication.addAction(self.actionRun)
        self.tb_communication.addAction(self.actionStop)

        self.retranslateUi(Editor_window)
        QtCore.QObject.connect(self.actionRedo, QtCore.SIGNAL(_fromUtf8("triggered()")), self.textEdit.redo)
        QtCore.QObject.connect(self.actionUndo, QtCore.SIGNAL(_fromUtf8("triggered()")), self.textEdit.undo)
        QtCore.QObject.connect(self.actionClear, QtCore.SIGNAL(_fromUtf8("triggered()")), self.textEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(Editor_window)

    def retranslateUi(self, Editor_window):
        Editor_window.setWindowTitle(_translate("Editor_window", "Editor", None))
        self.textEdit.setPlainText(_translate("Editor_window", "10 ", None))
        self.tb_files.setWindowTitle(_translate("Editor_window", "toolBar", None))
        self.tb_edit.setWindowTitle(_translate("Editor_window", "toolBar_2", None))
        self.tb_communication.setWindowTitle(_translate("Editor_window", "toolBar_3", None))
        self.actionOpen.setText(_translate("Editor_window", "Open", None))
        self.actionOpen.setToolTip(_translate("Editor_window", "Open file", None))
        self.actionOpen.setShortcut(_translate("Editor_window", "Ctrl+O", None))
        self.actionSave.setText(_translate("Editor_window", "Save", None))
        self.actionSave.setToolTip(_translate("Editor_window", "Save file", None))
        self.actionSave.setShortcut(_translate("Editor_window", "Ctrl+S", None))
        self.actionClear.setText(_translate("Editor_window", "Clear", None))
        self.actionClear.setToolTip(_translate("Editor_window", "Clear workspace", None))
        self.actionUpload.setText(_translate("Editor_window", "Upload", None))
        self.actionUpload.setToolTip(_translate("Editor_window", "Upload program to robot", None))
        self.actionRun.setText(_translate("Editor_window", "Run", None))
        self.actionRun.setToolTip(_translate("Editor_window", "Run uploaded program", None))
        self.actionRedo.setText(_translate("Editor_window", "Redo", None))
        self.actionRedo.setToolTip(_translate("Editor_window", "Redo", None))
        self.actionRedo.setShortcut(_translate("Editor_window", "Ctrl+Y", None))
        self.actionUndo.setText(_translate("Editor_window", "Undo", None))
        self.actionUndo.setToolTip(_translate("Editor_window", "Undo", None))
        self.actionUndo.setShortcut(_translate("Editor_window", "Ctrl+Z", None))
        self.actionStop.setText(_translate("Editor_window", "Stop", None))
        self.actionStop.setToolTip(_translate("Editor_window", "Stop execution of program", None))

import icon_pack_rc
