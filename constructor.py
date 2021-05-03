# coding: utf-8
# !/usr/local/bin/python3
import random

# We use the format method for each sentences because it allows us to set  where the selected word will be added
sentences = [format("{} c’est une bonne personne mais pas du tout"),
             format("demande à ton médecin si {} est bon pour toi"),
             format("je bois pour oublier {}"),
             format("regarder {} permet de me calmer"),
             format("le cadeau parfait pour une femme qui a déjà tout {}"),
             format("l’Egypte a les pyramides et la France {}"),
             format("didier Raoult a inventé {} contre le coronavirus"),
             format("{}, ça fond dans la bouche, pas dans la main"),
             format("{}, c'est encore meilleur la 2ème fois"),
             format("mon petit déjeuner préféré, c'est {}"),
             format("le 7ème jour Dieu créa {}"),
             format("je bois pour oublier {}"),
             format("{} me donne des gaz incontrôlables"),
             format("{} pour les nuls, le livre idéal pour la fête de mères"),
             format("{} ça a l'air marrant, mais en fait ça fait mal"),
             format("entre {} et une vie de famille, il faut choisir"),
             format("{} c'est tellement ton père !"),
             format("pour me faire pardonner je te propose {}"),
             format("{} La plus grande différence entre les hommes et les femmes"),
             format("{}, rien de mieux pour briser la glace"),
             format("{} c’est tout ce que je demande"),
             format("{} challenge accepted"),
             format("bon vent et gare à toi {} est si vite arrivée"),
             format("{} c’est comme une bonne guerre, ça forge la jeunesse"),
             format("râté la naissance de son fils pour {} à la rigueur ça peut se comprendre"),
             format("nouvelle émission de téléréalité les ch'tis et {}"),
             format("juda trahit Jésus lorsqu’il a découvert {}"),
             format("ma meilleure amie m’a avouée qu’elle kiffait {}"),
             format("quand j’étais petit, les autres voulaient être pompier, moi ce que je voulais c’est {}"),
             format("après 20 ans de débat, l’assemblée a enfin voté que {}"),
             format("scandale à Roubaix un professeur montre {} à ses élèves"),
             format("demande à ton médecin si {} est bon pour toi"),
             format("{} m’a appris le sens de la vie"),
             format("{} me scotch aux lunettes de toilette"),
             format("{} le meilleur livre pour la fête des pères"),
             format("{} le meilleur livre pour la fête des mères"),
             format("{} bon de la première cuillère jusqu’à la dernière goutte"),
             format("{} c’est triste mais drôle en même temps"),]

words = [format("une odeur de moule"),
        format("les vegans"),
        format("nos ancêtres les gaulois"),
        format("un cours d’aqua-poney"),
        format("un prêtre"),
        format("la messe du dimanche"),
        format("hitler"),
        format("ma bite"),
        format("les derniers centimètres"),
        format("un autiste"),
        format("faire l'hélicoptère devant sa mère"),
        format("maitre Gims"),
        format("une vegan qui se demande si elle peut avaler"),
        format("recoucher avec son ex"),
        format("jouir en 30s et s'en taper"),
        format("l'haleine du prof de maths"),
        format("une sodomie surprise"),
        format("traire une femme qui allaite"),
        format("des testicules trop pleines"),
        format("un kebab de pangolin"),
        format("ouvrir un compte en Suisse"),
        format("un cancer de la prostate"),
        format("mon ex"),
        format("300 matelots en rut après 6 mois en haute mer"),
        format("jean-Yves le Drian"),
        format("l'oeil de verre de Jean Marie le Pen"),
        format("un camembert bien coulant"),
        format("brontis"),
        format("une pièce, une cigarette ou un ticket restaurant"),
        format("la coulante"),
        format("les longues caresses de papy"),
        format("un long bain de minuit"),
        format("la sortie d'école"),
        format("ebola"),
        format("une mutation à Auxerre"),
        format("l'hygiène bucco-dentaire"),
        format("pisser face au vent"),
        format("la tribu de Dana"),
        format("1.5L de coca"),
        format("une odeur de moule"),
        format("les vegans"),
        format("nos ancêtres les Gaulois"),
        format("un cours d'aqua-poney"),
        format("un prêtre"),
        format("la messe du dimanche"),
        format("une sonde anale"),
        format("mon kiné"),
        format("un cactus dans le salon"),
        format("laisser ses chaussettes sécher à la fêntre"),
        format("un repas de famille avec ton oncle raciste"),
        format("le coming-out de mon frère"),
        format("le chien de la voisine"),
        format("les Roms"),
        format("une partouze masquée avec François Hollande"),
        format("pierre ménès que a la gastro"),
        format("des dreads sous les aisselles"),
        format("jouer à cache-cache contre Nordhal Lelandais"),
        format("regarder Games of Thrones"),
        format("les aventures de Winnie l'Ourson"),
        format("compter jusqu'à 3 avec Franklin"),
        format("souffler dans la chicha"),
        format("les phantoms"),
        format("tirer la chasse d'eau"),
        format("bernard Tapis"),
        format("20cm de bonheur"),]


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
print(play)