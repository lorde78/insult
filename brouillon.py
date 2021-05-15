# prop2 = QPushButton(self)
# prop2.setStyleSheet("QPushButton{background-color: white; border: 4px solid "+var.degrade+"; border-radius: 15px;color:"+var.degrade+"}QPushButton:pressed {background-color: "+var.degrade+"; border: 1px solid "+var.degrade+"; border-radius: 15px; color: white}")
# prop2.setMaximumSize(QtCore.QSize(300, 30))
# prop2.setGeometry(QtCore.QRect(30, 490, 300, 201))
# word = Constructor.test_choose_word(words)
# self.mots.append(word)
# prop2.setText(word)
# word2 = word
# prop2.clicked.connect(lambda: Clicked(1,self))
# prop2.clicked.connect(lambda: score(word2,True))
# prop2.clicked.connect(lambda: Clicked2(self))
# prop2.clicked.connect(lambda: score(word2,False))

# prop3 = QPushButton(self)
# prop3.setStyleSheet("QPushButton{background-color: white; border: 4px solid "+var.degrade+"; border-radius: 15px;color:"+var.degrade+"}QPushButton:pressed {background-color: "+var.degrade+"; border: 1px solid "+var.degrade+"; border-radius: 15px; color: white}")
# prop3.setMaximumSize(QtCore.QSize(300, 30))
# prop3.setGeometry(QtCore.QRect(30, 540, 300, 201))
# word = Constructor.test_choose_word(words)
# self.mots.append(word)
# prop3.setText(word)
# word3 = word
# prop3.clicked.connect(lambda: Clicked(2,self))
# prop3.clicked.connect(lambda: score(word3,True))
# prop3.clicked.connect(lambda: Clicked2(self))
# prop3.clicked.connect(lambda: score(word3,False))

# prop4 = QPushButton(self)
# prop4.setStyleSheet("QPushButton{background-color: white; border: 4px solid "+var.degrade+"; border-radius: 15px;color:"+var.degrade+"}QPushButton:pressed {background-color: "+var.degrade+"; border: 1px solid "+var.degrade+"; border-radius: 15px; color: white}")
# prop4.setMaximumSize(QtCore.QSize(300, 30))
# prop4.setGeometry(QtCore.QRect(30, 590, 300, 201))
# word = Constructor.test_choose_word(words)
# self.mots.append(word)
# prop4.setText(word)
# word4 = word
# prop4.clicked.connect(lambda: Clicked(3,self))
# prop4.clicked.connect(lambda: score(word4,True))
# prop4.clicked.connect(lambda: Clicked2(self))
# prop4.clicked.connect(lambda: score(word4,False))


# def score(motChoisi, Bool):
#     global resultScore
#     scorePlayer = 0
#     scoreBot = 0
#     if Bool:
#             toggleMot = motChoisi
#             toggleScore = scorePlayer
#             resultScore = 0
            
#     else:
#             toggleMot = motBot
#             toggleScore = scoreBot
#     i = 0
#     alors = "z"
#     while i < len(Pcat1):
#             if Pcat1[i] == returned_sentence:
#                     alors = "a"
#             i += 1
#     if alors == "z":
#             j = 0
#             while j < len(Pcat2):
#                     if Pcat2[j] == returned_sentence:
#                             alors = "b"
#                     j += 1
#     if alors == "z":
#             k = 0
#             while k < len(Pcat3):
#                     if Pcat3[k] == returned_sentence:
#                             alors = "c"
#                     k += 1
#     print(alors)
#     l = 0
#     donc = "y"
#     while l < len(Mcat1):
#             if Mcat1[l] == toggleMot:
#                     donc = "d"
#             l += 1
#     if donc == "y":    
#             m = 0
#             while m < len(Mcat2):
#                     if Mcat2[m] == toggleMot:
#                             donc == "e"
#                     m += 1        
#     if donc == "y":
#             n = 0
#             while n < len(Mcat3):
#                     if Mcat3[n] == toggleMot:
#                             donc = "f"
#                     n += 1
#     print(donc)

#     valuable = 0
#     toggleScore = valuable + points[toggleMot]
#     if alors == "a" and donc == "d":
#             toggleScore = toggleScore*2
#     elif alors == "a" and donc == "f":
#             toggleScore = toggleScore*1.5
#     elif alors == "b" and donc == "e":
#             toggleScore = toggleScore*2
#     elif alors == "c" and donc == "e":
#             toggleScore = toggleScore*2
#     elif alors == "c" and donc == "d":
#             toggleScore = toggleScore*1.5
#     elif alors == "c" and donc == "f":
#             toggleScore = toggleScore*1.5
#     print(toggleScore)
    
#     if resultScore == 0:
#             resultScore = toggleScore
            
#     else:
#             total = resultScore - toggleScore
#             print(total)
#             if total < 0 :
#                     Victory(False)
#                     print("victoire du Bot")
#                     VictoirePartie(self)
                    
#             if total > 0 :
#                     Victory(True)
#                     print("victoire du Joueur")
#                     VictoirePartie(self)
                            
#             if total == 0 :
#                     print("Egalite")
#                     VictoirePartie(self) 
#     print("Score:"+resultScore)
#     return resultScore