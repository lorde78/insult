from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
    ##Variables
import variable as var
styleButtonHome = "QPushButton {background-color: white; border: 1px solid "+var.degrade+"; border-radius: 15px; color: "+var.degrade+";font-weight:bold}""QPushButton:pressed {background-color: "+var.degrade+"; border: 1px solid "+var.degrade+"; border-radius: 15px; color: white}"
    
    
class AskingNamePage():
    
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

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(0, 35))
        self.label.setMaximumSize(QtCore.QSize(500, 30))
        self.label.setStyleSheet("background-color: "+var.degrade+"; border: 1px solid "+var.degrade+"; border-radius: 15px; color: white; font-size: 17px ")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setText("User-name :")

        self.layout_frame1.addWidget(self.label)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, 15, 0, 35)
        self.horizontalLayout.setSpacing(18)

        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit.setStyleSheet("background-color: white; border-radius: 15px; color: blue")
        self.lineEdit.setMaxLength(10)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setPlaceholderText("(max.10charact.)")
        self.lineEdit.textChanged.connect(Surnom)


        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setMaximumSize(QtCore.QSize(35, 35))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(var.path+"/images/Autre/icon-select.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(50, 30))
        self.pushButton.setCheckable(True)
        self.pushButton.setChecked(False)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(PressedButton_OK)
        self.pushButton.clicked.connect(self.close)

        self.horizontalLayout.addWidget(self.pushButton)
        self.layout_frame1.addLayout(self.horizontalLayout)

        
########################################################################

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


Username = "coucou"
def Surnom(self):
    global Username
    Username = self
    print(Username)
    return Username

from soloGameMAJ_V2 import *
from Mwindow import MWindow

window1 = MWindow()    
def PressedButton_OK():
    print("Solo Game Start")
    SoloGame.__init__(window1)

import homePage_0
window2 = MWindow() 
def ReturnHome():
        print("return home")
        homePage_0.HomePage.__init__(window2)
    


   