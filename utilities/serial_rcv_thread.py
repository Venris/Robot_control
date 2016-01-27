from PyQt4.QtCore import QThread,pyqtSignal
import serial

class rcv_thread(QThread):

    rcv_data=pyqtSignal(str)

    def __init__(self,port):
        # super(rcv_thread,self).__init__()
        QThread.__init__(self)
        self.isAlive=True
        self.port=port

    def __del__(self):
        self.isAlive=False
        self.wait()


    def run(self):
        while self.isAlive:
            # bytesToRead = self.port.inWaiting()
            rcv=self.port.read_until(terminator=serial.CR)
            if rcv!=None and rcv!="" and rcv!=b"":
                # print (rcv)
                self.rcv_data.emit(rcv.decode("UTF-8"))
            self.msleep(100)

