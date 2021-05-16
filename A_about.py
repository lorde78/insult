from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
    ##Variables
import A_variable as var
styleButtonHome = "QPushButton {background-color: white; border: 1px solid "+var.degrade+"; border-radius: 15px; color: "+var.degrade+";font-weight:bold}""QPushButton:pressed {background-color: "+var.degrade+"; border: 1px solid "+var.degrade+"; border-radius: 15px; color: white}"

import A_homePage_0  as home

#import A_about as home

class AskingaBoutPage():
    
    def __init__ (self):
        self.setStyleSheet("background-color: white")
        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 310, 267, 191))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
 
        self.layout_frame2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.layout_frame2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.layout_frame2.setContentsMargins(0, 0, 0, 0)
        self.layout_frame2.setSpacing(0)

        #askingName(self)
        afficherTextAbout(self)
        home.LOGO_Bubbles(self)

        self.show()

def afficherTextAbout(self):
    self.okidoki = QtWidgets.QLabel(self)
    self.okidoki.setGeometry(QtCore.QRect(60, 280, 230, 80))
    self.okidoki.setMaximumSize(QtCore.QSize(300, 100))
    self.okidoki.setAutoFillBackground(False)
    self.okidoki.setStyleSheet("background-color: "+var.degrade+"; border: 4px solid white; border-radius: 5px;color: white;")
    self.okidoki.setAlignment(QtCore.Qt.AlignCenter)
    self.okidoki.setText("Bienvenue sur Cannibale Dungo")
 

    


   