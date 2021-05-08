# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import os
from constructor_class import Bot, Constructor
from sentences import sentences
from words import words
path = os.getcwd() ### Pour les images les chemins

degrade = '''qradialgradient(
        radius:3,
        stop:0 rgb(255, 119, 55), 
        stop:0.3 rgb(255, 48, 108),
        stop:0.6 rgb(200, 58, 180))
'''


class Ui_SoloGame(object):
    def setupUi(self, SoloGame):
        SoloGame.setObjectName("SoloGame")
        SoloGame.resize(360, 640)
        SoloGame.setMinimumSize(QtCore.QSize(360, 640))
        SoloGame.setMaximumSize(QtCore.QSize(360, 640))
        SoloGame.setStyleSheet("background: #FFFFFF;")
        self.Header = QtWidgets.QFrame(SoloGame)
        self.Header.setGeometry(QtCore.QRect(-1, -40, 362, 110))
        self.Header.setStyleSheet("QFrame{background-color: white; border: 1px solid "+degrade+";border-radius: 10px;}")
        self.Header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Header.setObjectName("Header")
        self.ProfilPic = QtWidgets.QLabel(self.Header)
        self.ProfilPic.setGeometry(QtCore.QRect(30, 55, 40, 40))
        self.ProfilPic.setStyleSheet("border: 3px solid "+degrade+";""border-radius: 20px; ")
        self.ProfilPic.setPixmap(QtGui.QPixmap(path+"/images/LOGO/logo_colore.png"))
        self.ProfilPic.setScaledContents(True)
        self.ProfilPic.setAlignment(QtCore.Qt.AlignCenter)
        self.ProfilPic.setWordWrap(False)
        self.ProfilPic.setObjectName("ProfilPic")
        self.frame = QtWidgets.QFrame(self.Header)
        self.frame.setGeometry(QtCore.QRect(60, 75, 15, 15))
        self.frame.setStyleSheet("background: #3DBC3A;""border: 1.5px solid #FFFFFF;""border-radius: 7px; ")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.nameAge = QtWidgets.QLabel(self.Header)
        self.nameAge.setGeometry(QtCore.QRect(80, 70, 61, 16))
        self.nameAge.setStyleSheet("font-family: Reem Kufi;"
"font-style: normal;"
"font-weight: normal;"
"font-size: 14px;"
"line-height: 21px;"
"color:"+degrade+";"
"border:0px;")
        self.nameAge.setTextFormat(QtCore.Qt.AutoText)
        self.nameAge.setScaledContents(False)
        self.nameAge.setWordWrap(False)
        self.nameAge.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.nameAge.setObjectName("nameAge")
        self.home = QtWidgets.QLabel(self.Header)
        self.home.setGeometry(QtCore.QRect(260, 70, 41, 16))
        self.home.setStyleSheet("font-family: Reem Kufi;"
"font-style: normal;"
"font-weight: normal;"
"font-size: 14px;"
"line-height: 21px;"
"color:"+degrade+";"
"border:0px;")
        self.home.setTextFormat(QtCore.Qt.AutoText)
        self.home.setScaledContents(False)
        self.home.setWordWrap(False)
        self.home.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.home.setObjectName("home")
        self.pushButton = QtWidgets.QPushButton(self.Header)
        self.pushButton.setGeometry(QtCore.QRect(300, 62, 31, 31))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(path+"/images/Autre/home button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(25, 25))
        self.pushButton.setCheckable(False)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.panneauInf = QtWidgets.QFrame(SoloGame)
        self.panneauInf.setGeometry(QtCore.QRect(0, 410, 360, 230))
        self.panneauInf.setStyleSheet("QFrame{background-color: "+degrade+";""border-radius: 10px;}")
        self.panneauInf.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.panneauInf.setFrameShadow(QtWidgets.QFrame.Raised)
        self.panneauInf.setObjectName("panneauInf")
        self._sur10_3 = QtWidgets.QFrame(self.panneauInf)
        self._sur10_3.setGeometry(QtCore.QRect(30, 40, 301, 33))
        self._sur10_3.setStyleSheet("QFrame{background-color: white; border: 4px solid "+degrade+";""border-radius: 16px;}")
        self._sur10_3.setObjectName("_sur10_3")
        self.label_4 = QtWidgets.QLabel(self._sur10_3)
        self.label_4.setGeometry(QtCore.QRect(30, 5, 241, 21))
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet("font-family: Reem Kufi;"
"font-style: normal;"
"font-weight: bold;"
"font-size: 14px;"
"line-height: 21px;"
"color:"+degrade+";"
"border:0px;"
"background:transparent;"
"font-weight: bold;"
"")
        self.label_4.setTextFormat(QtCore.Qt.PlainText)
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setIndent(0)
        self.label_4.setObjectName("label_4")
        self._sur10_4 = QtWidgets.QFrame(self.panneauInf)
        self._sur10_4.setGeometry(QtCore.QRect(30, 80, 301, 33))
        self._sur10_4.setStyleSheet("QFrame{background-color: white; border: 4px solid "+degrade+";""border-radius: 16px;}")
        self._sur10_4.setObjectName("_sur10_4")
        self.label_5 = QtWidgets.QLabel(self._sur10_4)
        self.label_5.setGeometry(QtCore.QRect(30, 5, 241, 21))
        self.label_5.setAutoFillBackground(False)
        self.label_5.setStyleSheet("font-family: Reem Kufi;"
"font-style: normal;"
"font-weight: bold;"
"font-size: 14px;"
"line-height: 21px;"
"color:"+degrade+";"
"border:0px;"
"background:transparent;"
"font-weight: bold;"
"")
        self.label_5.setTextFormat(QtCore.Qt.PlainText)
        self.label_5.setScaledContents(False)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setIndent(0)
        self.label_5.setObjectName("label_5")
        self._sur10_5 = QtWidgets.QFrame(self.panneauInf)
        self._sur10_5.setGeometry(QtCore.QRect(30, 120, 301, 33))
        self._sur10_5.setStyleSheet("QFrame{background-color: white; border: 4px solid "+degrade+";""border-radius: 16px;}")
        self._sur10_5.setObjectName("_sur10_5")
        self.label_6 = QtWidgets.QLabel(self._sur10_5)
        self.label_6.setGeometry(QtCore.QRect(30, 5, 241, 21))
        self.label_6.setAutoFillBackground(False)
        self.label_6.setStyleSheet("font-family: Reem Kufi;"
"font-style: normal;"
"font-weight: bold;"
"font-size: 14px;"
"line-height: 21px;"
"color:"+degrade+";"
"border:0px;"
"background:transparent;"
"font-weight: bold;"
"")
        self.label_6.setTextFormat(QtCore.Qt.PlainText)
        self.label_6.setScaledContents(False)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setIndent(0)
        self.label_6.setObjectName("label_6")
        self._sur10_6 = QtWidgets.QFrame(self.panneauInf)
        self._sur10_6.setGeometry(QtCore.QRect(30, 160, 301, 33))
        self._sur10_6.setStyleSheet("QFrame{background-color: white; border: 4px solid "+degrade+";""border-radius: 16px;}")
        self._sur10_6.setObjectName("_sur10_6")
        self.label_8 = QtWidgets.QLabel(self._sur10_6)
        self.label_8.setGeometry(QtCore.QRect(30, 5, 241, 21))
        self.label_8.setAutoFillBackground(False)
        self.label_8.setStyleSheet("font-family: Reem Kufi;"
"font-style: normal;"
"font-weight: bold;"
"font-size: 14px;"
"line-height: 21px;"
"color:"+degrade+";"
"border:0px;"
"background:transparent;"
"font-weight: bold;"
"")
        self.label_8.setTextFormat(QtCore.Qt.PlainText)
        self.label_8.setScaledContents(False)
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setIndent(0)
        self.label_8.setObjectName("label_8")
        self.logoVide = QtWidgets.QLabel(SoloGame)
        self.logoVide.setGeometry(QtCore.QRect(150, 40, 60, 65))
        self.logoVide.setStyleSheet("background: transparent;")
        self.logoVide.setText("")
        self.logoVide.setPixmap(QtGui.QPixmap(path+"/images/LOGO/logo_vide.png"))
        self.logoVide.setScaledContents(True)
        self.logoVide.setAlignment(QtCore.Qt.AlignCenter)
        self.logoVide.setIndent(0)
        self.logoVide.setObjectName("logoVide")
        self._sur10 = QtWidgets.QFrame(SoloGame)
        self._sur10.setGeometry(QtCore.QRect(34, 390, 33, 33))
        self._sur10.setStyleSheet("QFrame{background-color: white; border: 1px solid "+degrade+";""border-radius: 16px;}")
        self._sur10.setObjectName("_sur10")
        self.label = QtWidgets.QLabel(self._sur10)
        self.label.setGeometry(QtCore.QRect(1, 9, 31, 16))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("font-family: Reem Kufi;"
"font-style: normal;"
"font-weight: normal;"
"font-size: 11px;"
"line-height: 21px;"
"color:"+degrade+";"
"border:0px;"
"background:transparent;"
"")
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setIndent(0)
        self.label.setObjectName("label")
        self._sur10_2 = QtWidgets.QFrame(SoloGame)
        self._sur10_2.setGeometry(QtCore.QRect(30, 100, 300, 100))
        self._sur10_2.setStyleSheet("QFrame{background-color: "+degrade+";""border: 4px solid white; border-radius: 16px;}")
        self._sur10_2.setObjectName("_sur10_2")
        self.label_2 = QtWidgets.QLabel(self._sur10_2)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 300, 42))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("font-family: Reem Kufi;"
"font-style: normal;"
"font-weight: bold;"
"font-size: 14px;"
"line-height: 21px;"
"color:white;"
"border:0px;"
"background:transparent;"
"font-weight: bold;"
"")
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setIndent(0)
        self.label_2.setObjectName("label_2")
        self.sendIcon = QtWidgets.QLabel(SoloGame)
        self.sendIcon.setGeometry(QtCore.QRect(290, 390, 33, 33))
        self.sendIcon.setStyleSheet("background:transparent;")
        self.sendIcon.setLineWidth(0)
        self.sendIcon.setText("")
        self.sendIcon.setPixmap(QtGui.QPixmap(path+"/images/Autre/envoyer_icon.png"))
        self.sendIcon.setScaledContents(False)
        self.sendIcon.setAlignment(QtCore.Qt.AlignCenter)
        self.sendIcon.setWordWrap(False)
        self.sendIcon.setObjectName("sendIcon")

        self.retranslateUi(SoloGame)
        QtCore.QMetaObject.connectSlotsByName(SoloGame)

    def retranslateUi(self, SoloGame):
        _translate = QtCore.QCoreApplication.translate
        SoloGame.setWindowTitle(_translate("SoloGame", "Form"))
        self.nameAge.setText(_translate("SoloGame", "Lucie, 20"))
        self.home.setText(_translate("SoloGame", "Home"))
        self.label_4.setText(_translate("SoloGame", Constructor.test_choose_word(words)))
        self.label_5.setText(_translate("SoloGame", Constructor.test_choose_word(words)))
        self.label_6.setText(_translate("SoloGame", Constructor.test_choose_word(words)))
        self.label_8.setText(_translate("SoloGame", Constructor.test_choose_word(words)))
        self.label.setText(_translate("SoloGame", "1/10"))
        self.label_2.setText(_translate("SoloGame", Constructor.random_sentence(sentences)))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SoloGame = QtWidgets.QWidget()
    ui = Ui_SoloGame()
    ui.setupUi(SoloGame)
    SoloGame.show()
    sys.exit(app.exec_())
