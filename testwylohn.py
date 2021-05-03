# coding: utf-8
# !/usr/local/bin/python3
import random
from points import *

words = ["une odeur de moule",
         "les vegans",
         "nos ancêtres les gaulois",
         "un cours d’aqua-poney",
         "un prêtre",
         "la messe du dimanche",
         "hitler",
         "ma bite",
         "20cm de bonheur",
         "les derniers centimètres",
         "un autiste"]


sentences = [format("{} c’est une bonne personne mais pas du tout"),
             format("demande à ton médecin si {} est bon pour toi"),
             format("je bois pour oublier {}"),
             format("regarder {} permet de me calmer"),
             format("le cadeau parfait pour une femme qui a déjà tout {}"),
             format("l’Egypte a les pyramides et la France {}"),
             format("didier Raoult a inventé {} contre le coronavirus"),
             format("{}, ça fond dans la bouche, pas dans la main"),
             format("{}, c'est encore meilleur la 2ème fois"),
             format("mon petit déjeuner préféré, c'est {}")]


# Using static methods because there is no init to set up but all the methods belongs to the construct Class

class Constructor:

    @staticmethod
    def choose_word(wordlist):

        word_choices = {}

        print("Choisissez maintenant un mot à placer dans la phrase")

        # Same proccess here to select the word
        for i in range(1, 6):
            word_choices["{0}".format(i)] = words.pop(words.index(random.choice(words)))

        # Then we display each key and value for the selection of the sentence for the words
        for key, value in word_choices.items():
            print(key, "=", value)

        # Testing the input before getting to the final step
        while True:
            try:
                # Input to select the sentence
                word_selection = int(input("\nChoisissez une valeur pour sélectioner le mot: \n"))
                assert word_selection > 0
                assert word_selection < 6

            except ValueError:

                print("Vous n'avez pas saisi une valeur valide")
                continue

            except AssertionError:

                print("Vous n'avez pas saisi une valeur entre 1 et 3")
                continue

            else:
                # Choosen word will be fetch in the word_choices{} with the selected input
                print("Vous avez choisis le mot: ", word_choices[f'{word_selection}'], "\n")

            word = word_choices[f'{word_selection}']

            i = 0
            alors = "z"
            while i < len(Pcat1):
                if Pcat1[i] == returned_sentence:
                    alors = "a"
                    i += 1
            if alors == "z":
                h = 0
                while h < len(Pcat2):
                    if Pcat2[h] == returned_sentence:
                        alors = "x"
                        h += 1
            if alors == "z":
                c = 0
                while c < len(Pcat3):
                    if Pcat3[c] == returned_sentence:
                        alors = "m"
                        c += 1
            print(alors)
            j = 0
            donc = "y"
            while j < len(Mcat1):
                if Mcat1[j] == mot:
                    donc = "d"
                    j += 1
            if donc == "y":    
                k = 0
                while k < len(Mcat2):
                    if Mcat2[k] == mot:
                        donc = "e"
                        k += 1        
            if donc == "y":
                l = 0
                while l < len(Mcat3):
                    if Mcat3[l] == mot:
                        donc = "f"
                        l += 1

            return word

    @staticmethod
    def random_sentence(sentences_list):
        sentence = sentences.pop(sentences.index(random.choice(sentences)))
        return sentence

    
returned_sentence = (Constructor.random_sentence(sentences))

class Bot:

    @staticmethod
    def bot_sentence():
        return returned_sentence.format(words.pop(words.index(random.choice(words))))


print(returned_sentence)

#print(Bot.bot_sentence())
print(Constructor.choose_word(words))