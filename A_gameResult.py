from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
import A_variable as var
import A_soloGameMAJ_V2 as game

class Game_Result:

    def __init__(self):
        print("GameRESULT")

        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(19, 130, 321, 251))
        self.layout_messagerie = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.layout_messagerie.setContentsMargins(0, 0, 0, 0)
        self.layout_messagerie.setSpacing(0)
        self.verticalLayoutWidget.setStyleSheet("Background:transparent")

        def RepUSER(self,phrase):
                print("RepUSER")
                self.repUser2 = QtWidgets.QLabel(self)
                self.repUser2.setGeometry(QtCore.QRect(50, 300, 300, 30))
                self.repUser2.setStyleSheet("background-color: white; border: 1px solid "+var.degrade+"; border-radius: 15px;color: blue;")
                self.repUser2.setAlignment(QtCore.Qt.AlignCenter)
                self.repUser2.setText(phrase)
                self.layout_messagerie.addWidget(self.repUser2)

        phraseReturn = game.SoloGame.__init__.Clicked.phrase
        RepUSER(self,phraseReturn)

        self.show()
    

