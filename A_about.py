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

        #askingName(self)
        afficherTextAbout(self)
        home.LOGO_Bubbles(self)

        self.show()

def afficherTextAbout(self):
    self.Sentence_ = QtWidgets.QLabel(self)
    self.Sentence_.setGeometry(QtCore.QRect(60, 280, 230, 80))
    self.Sentence_.setMaximumSize(QtCore.QSize(300, 100))
    self.Sentence_.setAutoFillBackground(False)
    self.Sentence_.setStyleSheet("background-color: "+var.degrade+"; border: 4px solid white; border-radius: 5px;color: white;")
    self.Sentence_.setAlignment(QtCore.Qt.AlignCenter)
    self.Sentence_.setText("Bienvenue sur Cannibale Dungo")


    


   