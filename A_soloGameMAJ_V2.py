from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
import A_variable as var
import A_askingName_0 as ask
from constructor_class import *
from sentences import sentences
from words import words
import time
import A_gameResult as result
from A_Mwindow import MWindow 
from points import *
from A_soloElements import *
from saut_ligne import Phrase_len


class SoloGame:

        def __init__(self):
                self.random_phrase = None
                self.mots = []
#HEADER###############################
                nameEnnemy = var.UserEnnemy
                Header(self,nameEnnemy)
                #HOME BUTTON
                returnhome = ask.ReturnHome
                Home_button(self,returnhome)
#PARTIE INF###############################################################
                Panneau(self)
###PROPOSITIONS#################################
                self.verticalLayoutWidget = QtWidgets.QWidget(self)
                self.verticalLayoutWidget.setGeometry(QtCore.QRect(19, 130, 321, 251))
                self.layout_messagerie = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
                self.layout_messagerie.setContentsMargins(0, 0, 0, 0)
                self.layout_messagerie.setSpacing(10)
                self.verticalLayoutWidget.setStyleSheet("Background:transparent")

                def AfficherREP (self,phraseReturn):
                        print("RepUSER")
                        self.repUser2 = QtWidgets.QLabel(self)
                        self.repUser2.setGeometry(QtCore.QRect(50, 300, 300, 30))
                        self.repUser2.setStyleSheet("background-color: white; border: 1px solid "+var.degrade+"; border-radius: 15px;color: blue;")
                        self.repUser2.setAlignment(QtCore.Qt.AlignCenter)
                        self.repUser2.setText(phraseReturn)
                        self.layout_messagerie.addWidget(self.repUser2)
                    

                windowResult = MWindow()    
                def Clicked(index,self):
                        print(self.mots[index])
                        print(self.random_phrase.format(self.mots[index]))
                        phrase = self.random_phrase.format(self.mots[index])
                        time.sleep(0)
                        AfficherREP (self,phrase)  

                def AfficherBOT (self,phraseBot):
                        print("RepBOT")
                        self.repUser2 = QtWidgets.QLabel(self)
                        self.repUser2.setGeometry(QtCore.QRect(50, 300, 300, 30))
                        self.repUser2.setStyleSheet("background-color: white; border: 1px solid "+var.degrade+"; border-radius: 15px;color: blue;")
                        self.repUser2.setAlignment(QtCore.Qt.AlignCenter)
                        self.repUser2.setText(phraseBot)
                        self.layout_messagerie.addWidget(self.repUser2)

                def Clicked2(self):
                        phraseBot = self.random_phrase.format(words.pop(words.index(random.choice(words))))
                        AfficherBOT(self,phraseBot)
                        return phraseBot
                

                prop1 = QPushButton(self)
                prop1.setStyleSheet("QPushButton{background-color: white; border: 4px solid "+var.degrade+"; border-radius: 15px;color:"+var.degrade+"}QPushButton:pressed {background-color: "+var.degrade+"; border: 1px solid "+var.degrade+"; border-radius: 15px; color: white}")
                prop1.setMaximumSize(QtCore.QSize(300, 30))
                prop1.setGeometry(QtCore.QRect(30, 440, 300, 201))
                word = Constructor.test_choose_word(words)
                self.mots.append(word)
                prop1.setText(word)
                word1 = word
                prop1.clicked.connect(lambda: Clicked(0,self))
                prop1.clicked.connect(lambda: score(word1,True))
                prop1.clicked.connect(lambda: Clicked2(self))
                prop1.clicked.connect(lambda: score(word1,False))

                prop2 = QPushButton(self)
                prop2.setStyleSheet("QPushButton{background-color: white; border: 4px solid "+var.degrade+"; border-radius: 15px;color:"+var.degrade+"}QPushButton:pressed {background-color: "+var.degrade+"; border: 1px solid "+var.degrade+"; border-radius: 15px; color: white}")
                prop2.setMaximumSize(QtCore.QSize(300, 30))
                prop2.setGeometry(QtCore.QRect(30, 490, 300, 201))
                word = Constructor.test_choose_word(words)
                self.mots.append(word)
                prop2.setText(word)
                word2 = word
                prop2.clicked.connect(lambda: Clicked(1,self))
                prop2.clicked.connect(lambda: score(word2,True))
                prop2.clicked.connect(lambda: Clicked2(self))
                prop2.clicked.connect(lambda: score(word2,False))

                prop3 = QPushButton(self)
                prop3.setStyleSheet("QPushButton{background-color: white; border: 4px solid "+var.degrade+"; border-radius: 15px;color:"+var.degrade+"}QPushButton:pressed {background-color: "+var.degrade+"; border: 1px solid "+var.degrade+"; border-radius: 15px; color: white}")
                prop3.setMaximumSize(QtCore.QSize(300, 30))
                prop3.setGeometry(QtCore.QRect(30, 540, 300, 201))
                word = Constructor.test_choose_word(words)
                self.mots.append(word)
                prop3.setText(word)
                word3 = word
                prop3.clicked.connect(lambda: Clicked(2,self))
                prop3.clicked.connect(lambda: score(word3,True))
                prop3.clicked.connect(lambda: Clicked2(self))
                prop3.clicked.connect(lambda: score(word3,False))

                prop4 = QPushButton(self)
                prop4.setStyleSheet("QPushButton{background-color: white; border: 4px solid "+var.degrade+"; border-radius: 15px;color:"+var.degrade+"}QPushButton:pressed {background-color: "+var.degrade+"; border: 1px solid "+var.degrade+"; border-radius: 15px; color: white}")
                prop4.setMaximumSize(QtCore.QSize(300, 30))
                prop4.setGeometry(QtCore.QRect(30, 590, 300, 201))
                word = Constructor.test_choose_word(words)
                self.mots.append(word)
                prop4.setText(word)
                word4 = word
                prop4.clicked.connect(lambda: Clicked(3,self))
                prop4.clicked.connect(lambda: score(word4,True))
                prop4.clicked.connect(lambda: Clicked2(self))
                prop4.clicked.connect(lambda: score(word4,False))

                print(self.mots)



                def score(motChoisi, Bool):
                        global resultScore
                        scorePlayer = 0
                        scoreBot = 0
                        if Bool:
                                toggleMot = motChoisi
                                toggleScore = scorePlayer
                                resultScore = 0
                                
                        else:
                                toggleMot = motBot
                                toggleScore = scoreBot
                        i = 0
                        alors = "z"
                        while i < len(Pcat1):
                                if Pcat1[i] == returned_sentence:
                                        alors = "a"
                                i += 1
                        if alors == "z":
                                j = 0
                                while j < len(Pcat2):
                                        if Pcat2[j] == returned_sentence:
                                                alors = "b"
                                        j += 1
                        if alors == "z":
                                k = 0
                                while k < len(Pcat3):
                                        if Pcat3[k] == returned_sentence:
                                                alors = "c"
                                        k += 1
                        print(alors)
                        l = 0
                        donc = "y"
                        while l < len(Mcat1):
                                if Mcat1[l] == toggleMot:
                                        donc = "d"
                                l += 1
                        if donc == "y":    
                                m = 0
                                while m < len(Mcat2):
                                        if Mcat2[m] == toggleMot:
                                                donc == "e"
                                        m += 1        
                        if donc == "y":
                                n = 0
                                while n < len(Mcat3):
                                        if Mcat3[n] == toggleMot:
                                                donc = "f"
                                        n += 1
                        print(donc)

                        valuable = 0
                        toggleScore = valuable + points[toggleMot]
                        if alors == "a" and donc == "d":
                                toggleScore = toggleScore*2
                        elif alors == "a" and donc == "f":
                                toggleScore = toggleScore*1.5
                        elif alors == "b" and donc == "e":
                                toggleScore = toggleScore*2
                        elif alors == "c" and donc == "e":
                                toggleScore = toggleScore*2
                        elif alors == "c" and donc == "d":
                                toggleScore = toggleScore*1.5
                        elif alors == "c" and donc == "f":
                                toggleScore = toggleScore*1.5
                        print(toggleScore)
                        
                        if resultScore == 0:
                                resultScore = toggleScore
                                
                        else:
                                total = resultScore - toggleScore
                                print(total)
                                if total < 0 :
                                        Victory(False)
                                        print("victoire du Bot")
                                        VictoirePartie(self)
                                        
                                if total > 0 :
                                        Victory(True)
                                        print("victoire du Joueur")
                                        VictoirePartie(self)
                                                 
                                if total == 0 :
                                        print("Egalite")
                                        VictoirePartie(self) 

                        return resultScore
                
                def Victory(gagnerPoint):
                        if gagnerPoint :
                                var.PointUser =+1
                                print(var.PointUser)
                        else :
                                var.PointEnnemy =+ 1
                                print(var.PointEnnemy)
                        
                        print("scoreUser", var.PointUser)
                        print("scoreBot", var.PointEnnemy)
                        
                
                def VictoirePartie(self):
                        if var.PointUser < 5 and var.PointEnnemy < 5 :
                                SoloGame.__init__(windowResult) # a modifier, parce que ca entraine la reinitialisation de tout le code surtout le score et ca passe sur une autre fenetre
                                self.close() 
                        elif var.PointUser == 5 :
                                print("Player Win")
                        elif var.PointEnnemy == 5 :
                                print("Bot Win")

            

#PHRASE A COMPLETER###############################################################
                random_phrase = Constructor.random_sentence(sentences)
                random_phrase = Phrase_len(random_phrase)
                PhraseToComplete(self,random_phrase)
#Enemy#############################
                Ennemy(self)
#POINTS / USERNAME###############################################################
                username = ask.Username
                User(self,username)
#LOGO###########
                Logo(self)
############
                self.show()
resultScore = 0

