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
                panneauBleu = Panneau(self)

###PROPOSITIONS#################################
                messagerie = Messagerie(self)
                
                
                
                def Clicked_ResultUser(who):
                        
                        if who == "bot":
                                print("Click BOT ")
                                var.PointEnnemy += 1
                                self.pointEnemy.setValue(var.PointEnnemy)


                        elif who == "user":
                                print("Click User")
                                var.PointUser += 1
                
                                self.pointUser.setValue(var.PointUser)
                  
                        self.repUser.close()
                        self.repBot.close()
                        # self.proposition1.setVisible(True)
                        # self.proposition2.setVisible(True)
                        # self.proposition3.setVisible(True)
                        # self.proposition4.setVisible(True)
                        
                        self.mots = []

                        nouv_propositons = Propositions(self)
                        

           

                def Clicked(index,self):

                        ##User
                        phrase = random_phrase.format(self.mots[index])
                        phrase = Phrase_len(phrase)
                        self.repUser = AfficherREP_(self,phrase)
                        self.repUser.clicked.connect(lambda: Clicked_ResultUser("user"))
                        print(self.mots)
                       
                        ##Bot
                        phraseBot = random_phrase.format(random.choice(words))
                        phraseBot = Phrase_len(phraseBot)
                        self.repBot = AfficherREP_(self,phraseBot)
                        self.repBot.clicked.connect(lambda: Clicked_ResultUser("bot"))

                        self.proposition1.close()
                        self.proposition2.close()
                        self.proposition3.close()
                        self.proposition4.close()

                        

                        
                def Propositions(self):
                        word = Constructor.test_choose_word(words)
                        self.mots.append(word)
                        self.proposition1 = Create_button(self,word,440)
                        self.proposition1.clicked.connect(lambda: Clicked(0,self))
                

                        word = Constructor.test_choose_word(words)
                        self.mots.append(word)
                        self.proposition2 = Create_button(self,word,490)
                        self.proposition2.clicked.connect(lambda: Clicked(1,self))

                        word = Constructor.test_choose_word(words)
                        self.mots.append(word)
                        self.proposition3 = Create_button(self,word,540)
                        self.proposition3.clicked.connect(lambda: Clicked(2,self))

                        word = Constructor.test_choose_word(words)
                        self.mots.append(word)
                        self.proposition4 = Create_button(self,word,590)
                        self.proposition4.clicked.connect(lambda: Clicked(3,self))
                
                Propositions(self)
            

                print(self.mots)

                        
                
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
                # Logo(self)
############
                self.show()
resultScore = 0

