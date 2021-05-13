from A_askingName_0 import AskingNamePage
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
    ##Variables
import A_variable as var
from A_askingName_0 import *
from A_Mwindow import MWindow
    
class HomePage():
        
        def __init__ (self):
                self.setStyleSheet("background-color: white")
                self.verticalLayoutWidget = QtWidgets.QWidget(self)
                self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 310, 267, 191))


                self.layout_frame1 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
                self.layout_frame1.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
                self.layout_frame1.setContentsMargins(0, 0, 0, 0)
                self.layout_frame1.setSpacing(0)

       
                Add_homeButtons(self)
        ##########
                LOGO_Bubbles(self)
                self.show()

def Add_homeButtons(self):
        #SOLO######_###
        self.pushButtonSolo = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButtonSolo.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButtonSolo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButtonSolo.setStyleSheet(var.styleButtonHome)
        self.pushButtonSolo.setText("SOLO")
        self.pushButtonSolo.clicked.connect(lambda: AfficherAskingPage(self))
        
        self.layout_frame1.addWidget(self.pushButtonSolo)

        #MULTI#########
        self.pushButtonMulti = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButtonMulti.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButtonMulti.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButtonMulti.setStyleSheet(var.styleButtonHome)
        self.pushButtonMulti.setText("MULTIJOUEURS")

        self.layout_frame1.addWidget(self.pushButtonMulti)

        #About#########
        
        self.pushButtonAbout = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButtonAbout.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButtonAbout.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButtonAbout.setStyleSheet(var.styleButtonHome)
        self.pushButtonAbout.setText("ABOUT")

        self.layout_frame1.addWidget(self.pushButtonAbout)

def LOGO_Bubbles (self):
        logoEmpty = QtWidgets.QLabel(self)
        logoEmpty.setGeometry(QtCore.QRect(100, 80, 171, 161))
        logoEmpty.setPixmap(QtGui.QPixmap(var.path+"/images/LOGO/logo-empty.png"))
        logoEmpty.setScaledContents(False)
        logoEmpty.setAlignment(QtCore.Qt.AlignCenter)

        titreCDungo = QtWidgets.QLabel(self)
        titreCDungo.setGeometry(QtCore.QRect(50, 230, 265, 51))
        titreCDungo.setPixmap(QtGui.QPixmap(var.path+"/images/LOGO/Cannibale_Dungo.png"))
        titreCDungo.setAlignment(QtCore.Qt.AlignCenter)

        #Bubbles#########
        bubbleLeft = QtWidgets.QLabel(self)
        bubbleLeft.setGeometry(QtCore.QRect(-20, 500, 141, 141))
        bubbleLeft.setPixmap(QtGui.QPixmap(var.path+"/images/Autre/bubble-1.png"))
        bubbleLeft.setScaledContents(True)
        bubbleLeft.setAlignment(QtCore.Qt.AlignCenter)
        bubbleLeft.setWordWrap(False)

        bubbleRight = QtWidgets.QLabel(self)
        bubbleRight.setGeometry(QtCore.QRect(290, -20, 111, 171))
        bubbleRight.setPixmap(QtGui.QPixmap(var.path+"/images/Autre/bubble-2.png"))


window = MWindow()
def AfficherAskingPage(self):
        self.close()
        AskingNamePage.__init__(window)
    



   