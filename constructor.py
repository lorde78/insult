# coding: utf-8
# !/usr/local/bin/python3
import random
from sentences import sentences
from words import words

def construct(sentences_list, wordlist):
    # The function construct is made to return a construced sentence using as parameters a list of
    # sentences and a list of words

    # Setting up two empty dictionnary who will later be filled with random sentences and words
    # sentences_choices = {}
    word_choices = {}

    # TODO faire pop les phrases choisies par random pour ne pas avoir de doublons

    # Quick check to see if the list are not empty
    if (len(sentences) & len(words)) > 0:

        print("La phrase à compléter:\n")

        # In this loop we are choosing randomly three sentences in the dictionnary sentences
        # and adding them one by one the dictionnary to get for each sentences a key and value
        # that we will use later to pick the sentence to build the final phrase
        #for i in range(1, 4):
        #    sentences_choices["{0}".format(i)] = random.choice(sentences)
        sentences_choices = random.choice(sentences)
        print(sentences_choices)
        # Then we display each key and value for the selection of the sentence
        #for key, value in sentences_choices.items():
        #    print(key, "=", value)

        # Testing the input before getting to the next step
        while True:
        #    try:
                # Input to select the sentence
        #        sentence_selection = int(input("\nChoisissez une valeur entre 1 et 3 pour sélectionner la phrase:\n"))
        #        assert sentence_selection > 0
        #        assert sentence_selection < 4

        #    except ValueError:

        #        print("Vous n'avez pas saisi une valeur valide")
        #        continue

        #    except AssertionError:

        #        print("Vous n'avez pas saisi une valeur entre 1 et 3")
        #        continue

        #    else:
                # If all exceotion are validated, the choosen sentence will be fetch in the sentences_choices{}
                # depending on the value input
        #        print("Vous avez choisis la phrase:", sentences_choices[f'{sentence_selection}'], "\n")

            #sentence = sentences_choices[f'{sentence_selection}']
            sentence = sentences_choices
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

                # The constructed sentence is the seletected sentence with the word put at the right place
                constructed_sentence = str(sentence.format(word).capitalize())

                # Then we finally retun the constructed sentence (but we could also just print it depending on the use)
                return constructed_sentence

    else:
        return "Listes vides"


play = construct(sentences, words)
print(construct(constructed_sentence))
print(play)