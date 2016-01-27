from PyQt4 import QtGui
from PyQt4.QtCore import pyqtSignal
from gui.editor import Ui_Editor_window
from time import strftime

class editor(QtGui.QMainWindow):
    send=pyqtSignal(str)
    program_sent=pyqtSignal(str,str)
    def __init__(self,parent=None):
        super(editor, self).__init__()

        self.ui=Ui_Editor_window()
        self.ui.setupUi(self)

        self.numberLines=0
        self.numberLinesLast=0
        self.set_signals()





    def set_signals(self):
        self.ui.actionSave.triggered.connect(self.saveFile)
        self.ui.actionUpload.triggered.connect(self.uploadProgram)
        self.ui.actionRun.triggered.connect(self.runProgram)
        self.ui.actionOpen.triggered.connect(self.openFile)
        self.ui.textEdit.blockCountChanged.connect(self.textChanged)
        self.ui.actionStop.triggered.connect(self.stopProgram)

        self.ui.actionRedo.triggered.connect(self.clear_window)
        # self.ui.actionUndo.triggered.connect(self.ui.textEdit.clear)
        # self.ui.actionClear.triggered.connect(self.ui.textEdit.clear)

    def saveFile(self):
        text=self.ui.textEdit.toPlainText()
        fileName=QtGui.QFileDialog.getSaveFileName(self,"Save Program","","Text (*.program)")
        try:
            f=open(str(fileName),mode="w",encoding='utf-8')
            f.write(text)
            f.close()
        except:
            pass

        pass

    def openFile(self):
        fileName = QtGui.QFileDialog.getOpenFileName(self,str("Open program"), "", str("Text (*.program)"))
        try:
            f=open(str(fileName),encoding="utf-8")
            text=f.read()
            f.close()

            self.ui.textEdit.setPlainText(text)
        except:
            pass

    def uploadProgram(self):
        text=self.ui.textEdit.toPlainText()
        count=0
        last_line=""
        for line in text.split("\n"):
            line=line.rstrip()
            if not line.isdigit() and not line.isalpha():
                self.send.emit(line)
                count+=1

        if count>0:
            self.program_sent.emit("{} || Program has been sent".format(strftime("%H:%M:%S")),'#0A0AA0')
        else:
            self.program_sent.emit("{} || No program written".format(strftime("%H:%M:%S")),'#0A0AA0')
        pass


    def runProgram(self):
        self.send.emit("RN")
        pass

    def stopProgram(self):
        self.send.emit("HLT")




    def textChanged(self):


        text=self.ui.textEdit.toPlainText()
        lines=text.split("\n")
        self.numberLines=self.ui.textEdit.blockCount()
        if self.numberLines>self.numberLinesLast:
            if len(lines[-1])==0:
                try:
                    if lines[-2].find(" ")!=-1:
                        nr=str(int(lines[-2][0:lines[-2].find(" ")])+10)+" "
                        # self.ui.textEdit.setPlainText(text+nr)
                        self.ui.textEdit.insertPlainText(nr)
                        # self.ui.textEdit.moveCursor(QtGui.QTextCursor.Down)
                        self.ui.textEdit.moveCursor(QtGui.QTextCursor.EndOfLine)
                except:
                    pass
        self.numberLinesLast=self.numberLines


    def clear_window(self):
        print("2")
        self.ui.textEdit.setPlainText("10 ")
        self.ui.textEdit.moveCursor(QtGui.QTextCursor.EndOfLine)

    def showEvent(self, *args, **kwargs):
        self.ui.textEdit.moveCursor(QtGui.QTextCursor.EndOfLine)

