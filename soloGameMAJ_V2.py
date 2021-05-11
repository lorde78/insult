

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
import variable as var
import askingName_0
from constructor_class import Bot, Constructor
from sentences import sentences
from words import words

class SoloGame:

    def __init__(self):
        self.random_phrase = None
        self.words = []
#HEADER###############################
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
        self.nameEnnemy.setText("Name ennemy")

        #HOME BUTTON
        self.pushButton = QtWidgets.QPushButton(self.Header)
        self.pushButton.setGeometry(QtCore.QRect(260, 60, 81, 31))
        self.pushButton.setStyleSheet("font-weight: normal;font-size: 14px;line-height: 21px;color:blue;border:0px;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(var.path+"/images/Autre/home_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setText(" Home")
        self.pushButton.clicked.connect(askingName_0.ReturnHome)
        self.pushButton.clicked.connect(self.close)

#PARTIE INF###############################################################

        self.panneauInf = QtWidgets.QFrame(self)
        self.panneauInf.setGeometry(QtCore.QRect(0, 410, 360, 230))
        self.panneauInf.setStyleSheet("QFrame{background-color: "+var.degrade+"; border-radius: 10px;}")
        self.panneauInf.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.panneauInf.setFrameShadow(QtWidgets.QFrame.Raised)

        
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.panneauInf)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(50, 20, 271, 201))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.layoutPropositions = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.layoutPropositions.setContentsMargins(0, 0, 0, 0)
        self.layoutPropositions.setSpacing(0)
        self.verticalLayoutWidget_2.setStyleSheet("Background:transparent")
        
        def Propositions(self):
                propositions = 4
                i = 0
                while i < propositions:
                        self.proposition = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
                        self.proposition.setEnabled(True)
                        self.proposition.setMaximumSize(QtCore.QSize(300, 30))
                        self.proposition.setSizeIncrement(QtCore.QSize(0, 0))
                        self.proposition.setBaseSize(QtCore.QSize(0, 0))
                        self.proposition.setStyleSheet("QPushButton{background-color: white; border: 4px solid "+var.degrade+"; border-radius: 15px;color:"+var.degrade+"}QPushButton:pressed {background-color: "+var.degrade+"; border: 1px solid "+var.degrade+"; border-radius: 15px; color: white}")
                        word = Constructor.test_choose_word(words)
                        self.words.append(word)
                        self.proposition.setText(word)
                        self.proposition.setAutoDefault(False)
                        # self.proposition.clicked.connect(askingName_0.ReturnHome)
                        # self.proposition.clicked.connect(self.close)
                        
                        self.layoutPropositions.addWidget(self.proposition)
                        i+=1
        Propositions(self)

        self.ProfilPic_2 = QtWidgets.QLabel(self)
        self.ProfilPic_2.setGeometry(QtCore.QRect(30, 390, 40, 40))
        self.ProfilPic_2.setStyleSheet(var.styleProfilPic)
        self.ProfilPic_2.setPixmap(QtGui.QPixmap(var.PicEnnemy))
        self.ProfilPic_2.setScaledContents(True)
        self.ProfilPic_2.setAlignment(QtCore.Qt.AlignCenter)


        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(19, 130, 321, 251))

#MESSAGERIE###############################################################

        self.layout_messagerie = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.layout_messagerie.setContentsMargins(0, 0, 0, 0)
        self.layout_messagerie.setObjectName("layout_messagerie")

#PHRASE A COMPLETER###############################################################

        self.Sentence_ = QtWidgets.QLabel(self)
        self.Sentence_.setGeometry(QtCore.QRect(80, 70, 230, 80))
        self.Sentence_.setAutoFillBackground(False)
        self.Sentence_.setStyleSheet("background-color: "+var.degrade+"; border: 4px solid white; border-radius: 16px;color: white;")
        self.Sentence_.setAlignment(QtCore.Qt.AlignCenter)
        self.random_phrase = Constructor.random_sentence(sentences)
        self.Sentence_.setText(self.random_phrase)

        # def showSurface(): ajoute un carré de discussion, montre la phrase avec le mot selectionnée en dessous de la premiere phrase de bot

        #         self.Sentence2_ = QtWidgets.QLabel(self)
        #         self.Sentence2_.setGeometry(QtCore.QRect(80, 70, 230, 80))
        #         self.Sentence2_.setAutoFillBackground(False)
        #         self.Sentence2_.setStyleSheet("background-color: "+var.degrade+"; border: 4px solid white; border-radius: 16px;color: white;")
        #         self.Sentence2_.setAlignment(QtCore.Qt.AlignCenter)
        #         self.random_phrase = Constructor.random_sentence(sentences)
        #         self.Sentence_.setText(self.random_phrase)

        self.picBot = QtWidgets.QLabel(self)
        self.picBot.setGeometry(QtCore.QRect(30, 70, 51, 51))
        self.picBot.setStyleSheet("background:transparent;")
        self.picBot.setPixmap(QtGui.QPixmap(var.path+"/images/Autre/Botpic.png"))
        self.picBot.setScaledContents(False)
        self.picBot.setAlignment(QtCore.Qt.AlignCenter)
        self.picBot.setObjectName("picBot")

#POINTS / USERNAME###############################################################
        self.pointEnemy = QtWidgets.QProgressBar(self)
        self.pointEnemy.setGeometry(QtCore.QRect(90, 400, 70, 20))
        self.pointEnemy.setStyleSheet(var.stylePointGame)
        self.pointEnemy.setMaximum(5)
        self.pointEnemy.setValue(var.PointEnnemy)
        self.pointEnemy.setTextVisible(False)


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
        self.UserName.setText(askingName_0.Username)

#LOGO###########
        self.titreLogo_transp = QtWidgets.QLabel(self)
        self.titreLogo_transp.setGeometry(QtCore.QRect(20, 180, 319, 149))
        self.titreLogo_transp.setStyleSheet("background: transparent;")
        self.titreLogo_transp.setPixmap(QtGui.QPixmap(var.path+"/images/LOGO/trans.png"))
        self.titreLogo_transp.setAlignment(QtCore.Qt.AlignCenter)
############

        self.show()



