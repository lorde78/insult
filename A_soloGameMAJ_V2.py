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
                messagerie = Messagerie(self)

                # messagerie.close()


                # def Clicked_ResultUser(who):

                #         if who == "bot":
                #                 print("Click BOT ")
                #         elif who == "user":
                #                 print("Click User")


                # def Clicked(index,self):
                #         ##User
                #         phrase = random_phrase.format(self.mots[index])
                #         phrase = Phrase_len(phrase)
                #         repUser = AfficherREP_(self,phrase)
                #         repUser.clicked.connect(lambda: Clicked_ResultUser("user"))

                #         ##Bot
                #         phraseBot = random_phrase.format(random.choice(words))
                #         phraseBot = Phrase_len(phraseBot)
                #         repBot = AfficherREP_(self,phraseBot)
                #         repBot.clicked.connect(lambda: Clicked_ResultUser("bot"))

                
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
                        time.sleep(1.5)
                        AfficherREP (self,phrase)
                        
                        

                        # result.Game_Result.__init__(windowResult)
                        # self.close()

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

                        # time.sleep(1.5)
                        # result.Game_Result.init(windowResult)
                        # self.close()
                        return phraseBot


                word = Constructor.test_choose_word(words)
                self.mots.append(word)
                proposition1 = Create_button(self,word,440)
                word1 = word
                proposition1.clicked.connect(lambda: Clicked(0,self))
                proposition1.clicked.connect(lambda: score(word1,True))
                proposition1.clicked.connect(lambda: Clicked2(self))
                proposition1.clicked.connect(lambda: score(word1,False))

                word = Constructor.test_choose_word(words)
                self.mots.append(word)
                proposition2 = Create_button(self,word,490)
                word2 = word
                proposition2.clicked.connect(lambda: Clicked(1,self))
                proposition2.clicked.connect(lambda: score(word2,True))
                proposition2.clicked.connect(lambda: Clicked2(self))
                proposition2.clicked.connect(lambda: score(word2,False))

                word = Constructor.test_choose_word(words)
                self.mots.append(word)
                proposition3 = Create_button(self,word,540)
                word3 = word
                proposition3.clicked.connect(lambda: Clicked(2,self))
                proposition3.clicked.connect(lambda: score(word3,True))
                proposition3.clicked.connect(lambda: Clicked2(self))
                proposition3.clicked.connect(lambda: score(word3,False))

                word = Constructor.test_choose_word(words)
                self.mots.append(word)
                proposition4 = Create_button(self,word,590)
                word4 = word
                proposition4.clicked.connect(lambda: Clicked(3,self))
                proposition4.clicked.connect(lambda: score(word4,True))
                proposition4.clicked.connect(lambda: Clicked2(self))
                proposition4.clicked.connect(lambda: score(word4,False))

                print(self.mots)

                motlol = "hello"
                ScoreBYNassim(motlol)

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
                                        # Victory(False)
                                        var.PointEnnemy += 1
                                        print(var.PointEnnemy,"victoire du Bot")
                                        # VictoirePartie(self)

                                if total > 0 :
                                        # Victory(True)
                                        var.PointUser += 1
                                        print(var.PointUser,"victoire du Joueur")
                                        # VictoirePartie(self)

                                if total == 0 :
                                        print("Egalite")
                                        # VictoirePartie(self)

                        return resultScore

                # def Victory(gagnerPoint):
                #         if gagnerPoint :
                #                 var.PointUser =+1
                #                 print(var.PointUser)
                #         else :
                #                 var.PointEnnemy =+ 1
                #                 print(var.PointEnnemy)

                #         print("scoreUser", var.PointUser)
                #         print("scoreBot", var.PointEnnemy)


                # def VictoirePartie(self):
                #         if var.PointUser < 5 and var.PointEnnemy < 5 :
                #                 SoloGame.__init__(windowResult) # a modifier, parce que ca entraine la reinitialisation de tout le code surtout le score et ca passe sur une autre fenetre
                #                 self.close()
                #         elif var.PointUser == 5 :
                #                 print("Player Win")
                #         elif var.PointEnnemy == 5 :
                #                 print("Bot Win")




#PHRASE A COMPLETER###############################################################
                self.Sentence_ = QtWidgets.QLabel(self)
                self.Sentence_.setGeometry(QtCore.QRect(80, 70, 230, 80))
                self.Sentence_.setMaximumSize(QtCore.QSize(300, 100))
                self.Sentence_.setStyleSheet("background-color: "+var.degrade+"; border: 4px solid white; border-radius: 5px;color: white;")
                self.Sentence_.setAlignment(QtCore.Qt.AlignCenter)
                self.random_phrase = Constructor.random_sentence(sentences)
                self.Sentence_.setText(self.random_phrase)
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

