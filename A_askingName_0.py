from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
    ##Variables
import A_variable as var
styleButtonHome = "QPushButton {background-color: white; border: 1px solid "+var.degrade+"; border-radius: 15px; color: "+var.degrade+";font-weight:bold}""QPushButton:pressed {background-color: "+var.degrade+"; border: 1px solid "+var.degrade+"; border-radius: 15px; color: white}"

from A_soloGameMAJ_V2 import *
from A_Mwindow import MWindow 

import A_homePage_0  as home

class AskingNamePage():
    
    def __init__ (self):
        self.setStyleSheet("background-color: white")
        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 310, 267, 191))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
 
        self.layout_frame2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.layout_frame2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.layout_frame2.setContentsMargins(0, 0, 0, 0)
        self.layout_frame2.setSpacing(0)

        askingName(self)
        home.LOGO_Bubbles(self)

        self.show()

def askingName(self):

    self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
    self.label.setMinimumSize(QtCore.QSize(0, 35))
    self.label.setMaximumSize(QtCore.QSize(500, 30))
    self.label.setStyleSheet("background-color: "+var.degrade+"; border: 1px solid "+var.degrade+"; border-radius: 15px; color: white; font-size: 17px ")
    self.label.setAlignment(QtCore.Qt.AlignCenter)
    self.label.setText("User-name :")

    self.layout_frame2.addWidget(self.label)

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
    self.layout_frame2.addLayout(self.horizontalLayout)


Username = "UserXX"
def Surnom(self):
    global Username
    Username = self
    print(Username)
    return Username


window1 = MWindow()   
def PressedButton_OK():
    print("Solo Game Start")
   
    SoloGame.__init__(window1)


window2 = MWindow() 
def ReturnHome():
        print("return home")
        home.HomePage.__init__(window2)
    


   