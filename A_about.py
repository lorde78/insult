from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from A_Mwindow import MWindow 
from A_soloGameMAJ_V2 import *
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
        returnhome = ReturnHome
        #askingName(self)
        afficherTextAbout(self)
        home.LOGO_Bubbles(self)
        Home_button(self, returnhome)

def afficherTextAbout(self):
    self.okidoki = QtWidgets.QLabel(self)
    self.okidoki.setGeometry(QtCore.QRect(60, 280, 240, 220))
    #self.okidoki.setMaximumSize(QtCore.QSize(300, 100))
    self.okidoki.setAutoFillBackground(False)
    self.okidoki.setStyleSheet("background-color: "+var.degrade+"; border: 4px solid white; border-radius: 5px;color: white;")
    self.okidoki.setAlignment(QtCore.Qt.AlignCenter)
    self.okidoki.setText("Bienvenue sur Cannibale Dungo\n\nAffrontez un bot\ndans la partie SOLO\nBattez votre ami\n en MULTIJOUEUR\n1 phrase à compléter\n4 propositions\nLe premier arrivé à 5 remporte la partie\n A vous de faire rire l'autre.\n\nNassim, Hugo, Wylohn, Basil")
 
def Home_button(self,returnhome):
    self.retourButton = QtWidgets.QPushButton(self)
    self.retourButton.setGeometry(QtCore.QRect(260, 500, 81, 31))
    self.retourButton.setStyleSheet("font-weight: normal;font-size: 14px;line-height: 21px;color:blue;border:0px;")
    #icon = QtGui.QIcon()
    #icon.addPixmap(QtGui.QPixmap(var.path+"/images/Autre/home_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    #self.pushButton.setIcon(icon)
    self.retourButton.setAutoDefault(False)
    self.retourButton.setText("Retour")
    self.retourButton.clicked.connect(returnhome)
    self.retourButton.clicked.connect(self.close)
    
window3 = MWindow() 
def ReturnHome():
        print("return home")
        home.HomePage.__init__(window3)


   