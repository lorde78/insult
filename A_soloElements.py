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
    self.pushButton.clicked.connect(lambda: returnhome(self))
    self.pushButton.clicked.connect(self.close)

def Panneau (self):
    self.panneauInf = QtWidgets.QFrame(self)
    self.panneauInf.setGeometry(QtCore.QRect(0, 410, 360, 250))
    self.panneauInf.setStyleSheet("QFrame{background-color: "+var.degrade+"; border-radius: 10px;}")
    self.panneauInf.setFrameShape(QtWidgets.QFrame.StyledPanel)
    self.panneauInf.setFrameShadow(QtWidgets.QFrame.Raised)

def Logo(self):
    self.titreLogo_transp = QtWidgets.QLabel(self)
    self.titreLogo_transp.setGeometry(QtCore.QRect(20, 180, 319, 149))
    self.titreLogo_transp.setStyleSheet("background: transparent;")
    self.titreLogo_transp.setPixmap(QtGui.QPixmap(var.path+"/images/LOGO/trans.png"))
    self.titreLogo_transp.setAlignment(QtCore.Qt.AlignCenter)

def PhraseToComplete(self,text):
        self.Sentence_ = QtWidgets.QLabel(self)
        self.Sentence_.setGeometry(QtCore.QRect(80, 60, 230, 80))
        self.Sentence_.setMaximumSize(QtCore.QSize(300, 100))
        self.Sentence_.setStyleSheet("background-color: "+var.degrade+"; border: 3px solid white; border-radius: 15px;color: white;")
        self.Sentence_.setAlignment(QtCore.Qt.AlignCenter)

        self.Sentence_.setText(text)

        self.picBot = QtWidgets.QLabel(self)
        self.picBot.setGeometry(QtCore.QRect(30, 70, 51, 51))
        self.picBot.setStyleSheet("background:transparent;")
        self.picBot.setPixmap(QtGui.QPixmap(var.path+"/images/Autre/Botpic.png"))
        self.picBot.setScaledContents(False)
        self.picBot.setAlignment(QtCore.Qt.AlignCenter)

        return self.Sentence_
####################################################################
def Ennemy (self):
    ProfilPic_2 = QtWidgets.QLabel(self)
    ProfilPic_2.setGeometry(QtCore.QRect(30, 390, 40, 40))
    ProfilPic_2.setStyleSheet(var.styleProfilPic)
    ProfilPic_2.setPixmap(QtGui.QPixmap(var.PicEnnemy))
    ProfilPic_2.setScaledContents(True)
    ProfilPic_2.setAlignment(QtCore.Qt.AlignCenter)
    #############
    self.pointEnemy = QtWidgets.QProgressBar(self)
    self.pointEnemy.setGeometry(QtCore.QRect(90, 400, 70, 20))
    self.pointEnemy.setStyleSheet(var.stylePointGame)
    self.pointEnemy.setMaximum(3)
    self.pointEnemy.setTextVisible(False)

    self.pointEnemy.setValue(var.PointEnnemy)

def User(self,nameUsername):
    self.pointUser = QtWidgets.QProgressBar(self)
    self.pointUser.setGeometry(QtCore.QRect(180, 400, 70, 20))
    self.pointUser.setStyleSheet(var.stylePointGame)
    self.pointUser.setMaximum(3)
    self.pointUser.setTextVisible(False)

    self.pointUser.setValue(var.PointUser)

    self.UserName = QtWidgets.QLabel(self)
    self.UserName.setGeometry(QtCore.QRect(259, 396, 95, 27))
    font = QtGui.QFont()
    font.setFamily("Shree Devanagari 714")
    font.setPointSize(14)
    self.UserName.setFont(font)
    self.UserName.setStyleSheet("background:white;color:blue;border: 1px solid "+var.degrade+";border-radius:13px;font-weight: semi-bold")
    self.UserName.setAlignment(QtCore.Qt.AlignCenter)
    self.UserName.setText(nameUsername)

###Messagerie#################################################################

def Messagerie(self):
    self.verticalLayoutWidget = QtWidgets.QWidget(self)
    self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 130, 320, 270))
    self.layout_messagerie = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
    self.layout_messagerie.setContentsMargins(0, 0, 0, 0)
    self.layout_messagerie.setSpacing(5)
    self.verticalLayoutWidget.setStyleSheet("Background:transparent")

    return self.verticalLayoutWidget



###PROPOSITIONS########################@
#position : 440 490 540 590
def Create_button(self,text,position):
        prop = QPushButton(self)
        prop.setStyleSheet("QPushButton{background-color: white; border: 1px solid "+var.degrade+"; border-radius: 15px;color:"+var.degrade+"}QPushButton:pressed {background-color: "+var.degrade+"; border: 1px solid white; border-radius: 15px; color: white}")
        prop.setMaximumSize(QtCore.QSize(300, 40))
        prop.setGeometry(QtCore.QRect(30, position, 300, 201))
        prop.setText(text)

        return prop


def AfficherREP_ (self,phraseReturn):

    rep = QPushButton(self)
    rep.setMaximumSize(QtCore.QSize(500, 70))
    rep.setText(phraseReturn)
    rep.setStyleSheet("QPushButton{background-color: white; border: 1px solid black; border-radius: 15px;color:black}QPushButton:pressed {background-color: green; border-radius: 15px; color: white; border: 1px solid white; }")
    self.layout_messagerie.addWidget(rep)

    return rep

####SCORE###############################################################
from constructor_class import *
from sentences import sentences
from words import words
from points import *


# def score(motChoisi, Bool):
#         global resultScore
#         scorePlayer = 0
#         scoreBot = 0
#         if Bool:
#                 toggleMot = motChoisi
#                 toggleScore = scorePlayer
#                 resultScore = 0
                
#         else:
#                 toggleMot = motBot
#                 toggleScore = scoreBot
#         i = 0
#         alors = "z"
#         while i < len(Pcat1):
#                 if Pcat1[i] == returned_sentence:
#                         alors = "a"
#                 i += 1
#         if alors == "z":
#                 j = 0
#                 while j < len(Pcat2):
#                         if Pcat2[j] == returned_sentence:
#                                 alors = "b"
#                         j += 1
#         if alors == "z":
#                 k = 0
#                 while k < len(Pcat3):
#                         if Pcat3[k] == returned_sentence:
#                                 alors = "c"
#                         k += 1
#         print(alors)
#         l = 0
#         donc = "y"
#         while l < len(Mcat1):
#                 if Mcat1[l] == toggleMot:
#                         donc = "d"
#                 l += 1
#         if donc == "y":    
#                 m = 0
#                 while m < len(Mcat2):
#                         if Mcat2[m] == toggleMot:
#                                 donc == "e"
#                         m += 1        
#         if donc == "y":
#                 n = 0
#                 while n < len(Mcat3):
#                         if Mcat3[n] == toggleMot:
#                                 donc = "f"
#                         n += 1
#         print(donc)

#         valuable = 0
#         toggleScore = valuable + points[toggleMot]
#         if alors == "a" and donc == "d":
#                 toggleScore = toggleScore*2
#         elif alors == "a" and donc == "f":
#                 toggleScore = toggleScore*1.5
#         elif alors == "b" and donc == "e":
#                 toggleScore = toggleScore*2
#         elif alors == "c" and donc == "e":
#                 toggleScore = toggleScore*2
#         elif alors == "c" and donc == "d":
#                 toggleScore = toggleScore*1.5
#         elif alors == "c" and donc == "f":
#                 toggleScore = toggleScore*1.5
#         print(toggleScore)
        
#         if resultScore == 0:
#                 resultScore = toggleScore
                
#         else:
#                 total = resultScore - toggleScore
#                 print(total)
#                 if total < 0 :
#                         Victory(False)
#                         print("victoire du Bot")
#                         VictoirePartie(self)
                        
#                 if total > 0 :
#                         Victory(True)
#                         print("victoire du Joueur")
#                         VictoirePartie(self)
                                        
#                 if total == 0 :
#                         print("Egalite")
#                         VictoirePartie(self) 

#         return resultScore


                        
                



