# coding: utf-8
# !/usr/local/bin/python3
import random
from words import words
from sentences import sentences
from points import Mcat1, Mcat2, Mcat3, Pcat1, Pcat2, Pcat3, points





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

                print("Vous n'avez pas saisi une valeur entre 1 et 5")
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
                if Mcat1[l] == word:
                    donc = "d"
                l += 1
            if donc == "y":    
                m = 0
                while m < len(Mcat2):
                    if Mcat2[m] == word:
                        donc == "e"
                    m += 1        
            if donc == "y":
                n = 0
                while n < len(Mcat3):
                    if Mcat3[n] == word:
                        donc = "f"
                    n += 1
            print(donc)

            valuable = 0
            score = valuable + points[word]
            if alors == "a" and donc == "d":
                score*2
            if alors == "a" and donc == "f":
                score*1.5
            elif alors == "b" and donc == "e":
                score*2
            elif alors == "c" and donc == "e":
                score*2
            elif alors == "c" and donc == "d":
                score*1.5
            elif alors == "c" and donc == "f":
                score*1.5
            print(score)
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
print(Bot.bot_sentence())
print(Constructor.choose_word(words))
