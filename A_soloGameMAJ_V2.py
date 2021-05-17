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
                self.end = False

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
                          
                                var.PointEnnemy += 1
                                self.pointEnemy.setValue(var.PointEnnemy)


                        elif who == "user":
                              
                                var.PointUser += 1
                
                                self.pointUser.setValue(var.PointUser)
                  
                        self.repUser.close()
                        self.repBot.close()
                        self.proposition1.setVisible(True)
                        self.proposition2.setVisible(True)
                        self.proposition3.setVisible(True)
                        self.proposition4.setVisible(True)

                        random_phrase2 = Constructor.random_sentence(sentences)
                        random_phrase2 = Phrase_len(random_phrase2)
                        PhraseToComplete(self,random_phrase2)

                        liste2 = []
                        word2 = Constructor.test_choose_word(words)
                        Propositions(self,liste2,word2)

                        NewGame(self)
                        
                def Clicked(index,self):
                        ##User
                        phrase = random_phrase.format(self.mots[index])
                        phrase = Phrase_len(phrase)
                        self.repUser = AfficherREP_(self,phrase)
                        self.repUser.clicked.connect(lambda: Clicked_ResultUser("user"))

                        ##Bot
                        phraseBot = random_phrase.format(random.choice(words))
                        phraseBot = Phrase_len(phraseBot)
                        self.repBot = AfficherREP_(self,phraseBot)
                        self.repBot.clicked.connect(lambda: Clicked_ResultUser("bot"))

                        self.proposition1.setVisible(False)
                        self.proposition2.setVisible(False)
                        self.proposition3.setVisible(False)
                        self.proposition4.setVisible(False)

                        self.Sentence_.close()

                        
                def Propositions(self,liste,word):
                    
                        liste.append(word)
                        self.proposition1 = Create_button(self,word,440)
                        self.proposition1.clicked.connect(lambda: Clicked(0,self))
                

                        word = Constructor.test_choose_word(words)
                        liste.append(word)
                        self.proposition2 = Create_button(self,word,490)
                        self.proposition2.clicked.connect(lambda: Clicked(1,self))

                        word = Constructor.test_choose_word(words)
                        liste.append(word)
                        self.proposition3 = Create_button(self,word,540)
                        self.proposition3.clicked.connect(lambda: Clicked(2,self))

                        word = Constructor.test_choose_word(words)
                        liste.append(word)
                        self.proposition4 = Create_button(self,word,590)
                        self.proposition4.clicked.connect(lambda: Clicked(3,self))

                word1 = Constructor.test_choose_word(words)

                Propositions(self,self.mots,word1)

                def VictoirePartie(self,value):
                        if var.PointUser == value :
                                print("PLAYER WIN")
                                self.close()
                                self.end = True
                                print(self.end)
                        elif var.PointEnnemy == value :
                                print("BOT WIN")
                                self.close()
                                self.end = True
                                print(self.end)

                VictoirePartie(self,3)
                # La liste de mots n'étant pas assez longue la partie va s'arrêter en cours de route, nous vous conseillons de modifier le paramètre VictoirePartie(self,3)

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


def NewGame(self):

        self.close()
        window1 = MWindow()
        if self.end == False:
                SoloGame.__init__(window1)

