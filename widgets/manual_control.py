from gui.manualControl import Ui_ManualControl
from PyQt4 import QtGui
from PyQt4.QtCore import pyqtSignal

class manual_control(QtGui.QWidget):
    send=pyqtSignal(str)
    # position=pyqtSignal(int)

    def __init__(self):
        super(manual_control, self).__init__()
        self.ui=Ui_ManualControl()
        self.ui.setupUi(self)

        self.rb_list=[self.ui.rb_joint_1,self.ui.rb_joint_2,self.ui.rb_joint_3,self.ui.rb_joint_4,self.ui.rb_joint_5,self.ui.rb_joint_6]
        self.setSignals()


    def setSignals(self):
        self.ui.pb_close_hand.clicked.connect(self.close_hand)
        self.ui.pb_open_hand.clicked.connect(self.open_hand)
        self.ui.pb_moveJoint.clicked.connect(self.move_joint)
        self.ui.pb_moveTool.clicked.connect(self.move_tool)
        self.ui.pb_moveXYZ.clicked.connect(self.move_xyz)
        self.ui.pb_movePos.clicked.connect(self.move_position)
        self.ui.pb_savePos.clicked.connect(self.save_position)
        self.ui.pb_setSpeed.clicked.connect(self.set_speed)

    def set_speed(self):
        speed=self.ui.scroll_speed.value()
        msg="SP {}".format(speed)
        self.send.emit(msg)
        pass

    def save_position(self):
        number=self.ui.sb_savePos.value()
        msg="HE {}".format(number)
        self.send.emit(msg)
        # self.position.emit(int(number))
        pass

    def move_position(self):
        number=self.ui.sb_movePos.value()
        msg="MO {}".format(number)
        self.send.emit(msg)
        pass

    def move_joint(self):
        for i,rb in enumerate(self.rb_list):
            if rb.isChecked():
                joint=i+1
        value=self.ui.scroll_joint.value()
        msg="DJ {},{}".format(joint,value)
        self.send.emit(msg)
        pass

    def move_tool(self):
        x=self.ui.sb_toolX.value()
        y=self.ui.sb_toolY.value()
        z=self.ui.sb_toolZ.value()
        # a=self.ui.sb_toolA.value()
        # b=self.ui.sb_toolB.value()
        # c=self.ui.sb_toolC.value()
        msg="DS {},{},{}".format(x,y,z)
        self.send.emit(msg)
        pass

    def move_xyz(self):
        x=self.ui.sb_xyzX.value()
        y=self.ui.sb_xyzY.value()
        z=self.ui.sb_xyzZ.value()
        # a=self.ui.sb_xyzA.value()
        # b=self.ui.sb_xyzB.value()
        # c=self.ui.sb_xyzC.value()
        msg="DW {},{},{}".format(x,y,z)
        self.send.emit(msg)
        pass

    def close_hand(self):
        self.send.emit("GO")

    def open_hand(self):
        self.send.emit("GC")
        pass





