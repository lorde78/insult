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
                

                def Clicked_ResultUser(phrase):
                        print("Click USER "+phrase)

                def Clicked_ResultBot():
                        print("Click BOT")


                def Clicked(index,self):

                        phrase = random_phrase.format(self.mots[index])
                        phrase = Phrase_len(phrase)
                        print(phrase)
                        repUser = AfficherREP_(self,phrase)
                        repUser.clicked.connect(lambda: Clicked_ResultUser("Hello"))
                        
                def Clicked_BOT():
                        ##Bot
                        phraseBot = random_phrase.format(random.choice(words))
                        phraseBot = Phrase_len(phraseBot)
                        repBot = AfficherREP_(self,phraseBot)
                        repBot.clicked.connect(lambda: Clicked_ResultBot())

                        


               
                word = Constructor.test_choose_word(words)
                self.mots.append(word)
                proposition1 = Create_button(self,word,440)
                proposition1.clicked.connect(lambda: Clicked(0,self))
                proposition1.clicked.connect(lambda: Clicked_BOT())

                word = Constructor.test_choose_word(words)
                self.mots.append(word)
                proposition2 = Create_button(self,word,490)
                proposition2.clicked.connect(lambda: Clicked(1,self))

                word = Constructor.test_choose_word(words)
                self.mots.append(word)
                proposition3 = Create_button(self,word,540)
                proposition3.clicked.connect(lambda: Clicked(2,self))

                word = Constructor.test_choose_word(words)
                self.mots.append(word)
                proposition4 = Create_button(self,word,590)
                proposition4.clicked.connect(lambda: Clicked(3,self))

                print(self.mots)

                motlol = "hello"
                ScoreBYNassim(motlol)

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
                                # SoloGame.__init__(windowResult) # a modifier, parce que ca entraine la reinitialisation de tout le code surtout le score et ca passe sur une autre fenetre
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

