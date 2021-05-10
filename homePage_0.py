from askingName_0 import AskingNamePage
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
    ##Variables
import variable as var
    
class HomePage():
    
    def __init__ (self):
        self.setStyleSheet("background-color: white")
        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 310, 267, 191))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.layout_frame1 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.layout_frame1.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.layout_frame1.setContentsMargins(0, 0, 0, 0)
        self.layout_frame1.setSpacing(0)
        self.layout_frame1.setObjectName("layout_frame1")

        self.pushButtonSolo = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButtonSolo.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButtonSolo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButtonSolo.setStyleSheet(var.styleButtonHome)
        self.pushButtonSolo.setText("SOLO")
        self.pushButtonSolo.clicked.connect(PressedButtonSolo)
        self.pushButtonSolo.clicked.connect(self.close)

        self.layout_frame1.addWidget(self.pushButtonSolo)

        self.pushButtonMulti = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButtonMulti.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButtonMulti.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButtonMulti.setStyleSheet(var.styleButtonHome)
        self.pushButtonMulti.setText("MULTIJOUEURS")

        self.layout_frame1.addWidget(self.pushButtonMulti)

        self.pushButtonAbout = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButtonAbout.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButtonAbout.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButtonAbout.setStyleSheet(var.styleButtonHome)
        self.pushButtonAbout.setText("ABOUT")

        self.layout_frame1.addWidget(self.pushButtonAbout)

        self.logoEmpty = QtWidgets.QLabel(self)
        self.logoEmpty.setGeometry(QtCore.QRect(100, 80, 171, 161))
        self.logoEmpty.setText("")
        self.logoEmpty.setPixmap(QtGui.QPixmap(var.path+"/images/LOGO/logo-empty.png"))
        self.logoEmpty.setScaledContents(False)
        self.logoEmpty.setAlignment(QtCore.Qt.AlignCenter)
        self.logoEmpty.setObjectName("logoEmpty")

        self.titreCDungo = QtWidgets.QLabel(self)
        self.titreCDungo.setGeometry(QtCore.QRect(50, 230, 265, 51))
        self.titreCDungo.setText("")
        self.titreCDungo.setPixmap(QtGui.QPixmap(var.path+"/images/LOGO/Cannibale_Dungo.png"))
        self.titreCDungo.setAlignment(QtCore.Qt.AlignCenter)
        self.titreCDungo.setObjectName("titreCDungo")

        self.bubbleLeft = QtWidgets.QLabel(self)
        self.bubbleLeft.setGeometry(QtCore.QRect(-20, 500, 141, 141))
        self.bubbleLeft.setPixmap(QtGui.QPixmap(var.path+"/images/Autre/bubble-1.png"))
        self.bubbleLeft.setScaledContents(True)
        self.bubbleLeft.setAlignment(QtCore.Qt.AlignCenter)
        self.bubbleLeft.setWordWrap(False)
        self.bubbleLeft.setObjectName("bubbleLeft")

        self.bubbleRight = QtWidgets.QLabel(self)
        self.bubbleRight.setGeometry(QtCore.QRect(290, -20, 111, 171))
        self.bubbleRight.setPixmap(QtGui.QPixmap(var.path+"/images/Autre/bubble-2.png"))
        self.bubbleRight.setObjectName("bubbleRight")

        self.show()

from askingName_0 import *
from Mwindow import MWindow
window = MWindow()

def PressedButtonSolo():
    AskingNamePage.__init__(window)
    



   