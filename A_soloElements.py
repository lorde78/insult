from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
import A_variable as var

def Header (self,nameEnnemy):
    self.Header = QtWidgets.QFrame(self)
    self.Header.setGeometry(QtCore.QRect(-1, -40, 362, 110))
    self.Header.setStyleSheet("QFrame{background-color: white; border: 1px solid "+var.degrade+"; border-radius: 10px;}")
    self.Header.setFrameShape(QtWidgets.QFrame.StyledPanel)
    self.Header.setFrameShadow(QtWidgets.QFrame.Raised)

    self.ProfilPic = QtWidgets.QLabel(self.Header)
    self.ProfilPic.setGeometry(QtCore.QRect(30, 55, 40, 40))
    self.ProfilPic.setStyleSheet(var.styleProfilPic)
    self.ProfilPic.setPixmap(QtGui.QPixmap(var.PicEnnemy))
    self.ProfilPic.setScaledContents(True)
    self.ProfilPic.setAlignment(QtCore.Qt.AlignCenter)

    self.online = QtWidgets.QFrame(self.Header)
    self.online.setGeometry(QtCore.QRect(60, 75, 15, 15))
    self.online.setStyleSheet("background: #3DBC3A;border: 1.5px solid #FFFFFF;border-radius: 7px; ")
    self.online.setFrameShape(QtWidgets.QFrame.StyledPanel)
    self.online.setFrameShadow(QtWidgets.QFrame.Raised)


    self.nameEnnemy = QtWidgets.QLabel(self.Header)
    self.nameEnnemy.setGeometry(QtCore.QRect(80, 70, 110, 16))
    self.nameEnnemy.setStyleSheet("font-weight: bold;font-size: 14px;line-height: 21px;color:blue;border:0px;")
    self.nameEnnemy.setTextFormat(QtCore.Qt.AutoText)
    self.nameEnnemy.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
    self.nameEnnemy.setText(nameEnnemy)

def Home_button(self,returnhome):
    self.pushButton = QtWidgets.QPushButton(self.Header)
    self.pushButton.setGeometry(QtCore.QRect(260, 60, 81, 31))
    self.pushButton.setStyleSheet("font-weight: normal;font-size: 14px;line-height: 21px;color:blue;border:0px;")
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(var.path+"/images/Autre/home_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.pushButton.setIcon(icon)
    self.pushButton.setAutoDefault(False)
    self.pushButton.setText(" Home")
    self.pushButton.clicked.connect(returnhome)
    self.pushButton.clicked.connect(self.close)

def Panneau (self):
    panneauInf = QtWidgets.QFrame(self)
    panneauInf.setGeometry(QtCore.QRect(0, 410, 360, 250))
    panneauInf.setStyleSheet("QFrame{background-color: "+var.degrade+"; border-radius: 10px;}")
    panneauInf.setFrameShape(QtWidgets.QFrame.StyledPanel)
    panneauInf.setFrameShadow(QtWidgets.QFrame.Raised)

def Logo(self):
    self.titreLogo_transp = QtWidgets.QLabel(self)
    self.titreLogo_transp.setGeometry(QtCore.QRect(20, 180, 319, 149))
    self.titreLogo_transp.setStyleSheet("background: transparent;")
    self.titreLogo_transp.setPixmap(QtGui.QPixmap(var.path+"/images/LOGO/trans.png"))
    self.titreLogo_transp.setAlignment(QtCore.Qt.AlignCenter)

def PhraseToComplete(self,random_phrase):
    self.Sentence_ = QtWidgets.QLabel(self)
    self.Sentence_.setGeometry(QtCore.QRect(80, 70, 230, 80))
    self.Sentence_.setMaximumSize(QtCore.QSize(300, 100))
    self.Sentence_.setStyleSheet("background-color: "+var.degrade+"; border: 4px solid white; border-radius: 5px;color: white;")
    self.Sentence_.setAlignment(QtCore.Qt.AlignCenter)
    self.Sentence_.setText(random_phrase)

    self.picBot = QtWidgets.QLabel(self)
    self.picBot.setGeometry(QtCore.QRect(30, 70, 51, 51))
    self.picBot.setStyleSheet("background:transparent;")
    self.picBot.setPixmap(QtGui.QPixmap(var.path+"/images/Autre/Botpic.png"))
    self.picBot.setScaledContents(False)
    self.picBot.setAlignment(QtCore.Qt.AlignCenter)
####################################################################
def Ennemy (self):
    self.ProfilPic_2 = QtWidgets.QLabel(self)
    self.ProfilPic_2.setGeometry(QtCore.QRect(30, 390, 40, 40))
    self.ProfilPic_2.setStyleSheet(var.styleProfilPic)
    self.ProfilPic_2.setPixmap(QtGui.QPixmap(var.PicEnnemy))
    self.ProfilPic_2.setScaledContents(True)
    self.ProfilPic_2.setAlignment(QtCore.Qt.AlignCenter)
    #############
    self.pointEnemy = QtWidgets.QProgressBar(self)
    self.pointEnemy.setGeometry(QtCore.QRect(90, 400, 70, 20))
    self.pointEnemy.setStyleSheet(var.stylePointGame)
    self.pointEnemy.setMaximum(5)
    self.pointEnemy.setValue(var.PointEnnemy)
    self.pointEnemy.setTextVisible(False)

def User(self,nameUsername):
    self.pointUser = QtWidgets.QProgressBar(self)
    self.pointUser.setGeometry(QtCore.QRect(180, 400, 70, 20))
    self.pointUser.setStyleSheet(var.stylePointGame)
    self.pointUser.setMaximum(5)
    self.pointUser.setValue(var.PointUser)
    self.pointUser.setTextVisible(False)

    self.UserName = QtWidgets.QLabel(self)
    self.UserName.setGeometry(QtCore.QRect(259, 396, 95, 27))
    font = QtGui.QFont()
    font.setFamily("Shree Devanagari 714")
    font.setPointSize(14)
    self.UserName.setFont(font)
    self.UserName.setStyleSheet("background:white;color:blue;border: 1px solid "+var.degrade+";border-radius:13px;font-weight: semi-bold")
    self.UserName.setAlignment(QtCore.Qt.AlignCenter)
    self.UserName.setText(nameUsername)

####################################################################



