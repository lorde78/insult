#import points
Mcat1 = ["une odeur de moule",
    "les vegans", 
    "nos ancêtres les gaulois", 
    "un cours d’aqua-poney",
    "un prêtre",
    "la messe du dimanche",
    "Les derniers centimètres",
    "Maître Gims",
    "L'haleine du prof de maths",
    "Un kebab de pangolin",
    "Mon ex",
    "300 matelots en rut après 6 mois en haute mer",
    "Jean-Yves le Drian",
    "L'oeil de verre de Jean Marie le Pen",
    "Un camembert bien coulant",
    "Brontis",
    "Une pièce, une cigarette ou un ticket restaurant",
    "Un long bain de minuit",
    "La sortie d'école",
    "Ebola",
    "Une mutation à Auxerre",
    "L'hygiène bucco-dentaire",
    "La tribu de Dana",
    "1.5L de coca",
    "Une odeur de moule",
    "Un cours d'aqua-poney",
    "Mon kiné",
    "Un cactus dans le salon",
    "Le coming-out de mon frère",
    "Le chien de la voisine",
    "Les Roms",
    "Pierre ménès que a la gastro",
    "Des dreads sous les aisselles",
    "Les aventures de Winnie l'Ourson",
    "Les fantômes",
    "Bernard Tapis",
    "HETIC"]

Mcat2 = ["Jouer à cache-cache contre Nordhal Lelandais",
"Faire l'hélicoptère devant sa mère",
"Regarder Games of Thrones",
"Tirer la chasse d'eau",
"Recoucher avec son ex",
"Jouir en 30s et s'en taper",
"Laisser ses chaussettes sécher à la fenêtre",
"Traire une femme qui allaite",
"Souffler dans la chicha",
"Pisser face au vent",
"Compter jusqu'à 3 avec Franklin",
"Ouvrir un compte en Suisse"]

Mcat3 = ["Hitler",
"Ma bite",
"20 cm de bonheur",
"Un autiste",
"Une vegan qui se demande si elle peut avaler",
"Une partouze masquée avec François Hollande",
"Une sodomie surprise",
"Des testicules trop pleines",
"Une sonde anale",
"Un cancer de la prostate",
"Les longues caresses de papy",
"La coulante",
"Un repas de famille avec ton oncle raciste"]

deck = []

for i in range (0, len(Mcat1)):
            for j in range (0, len(Mcat2)):
                for k in range (0, len(Mcat3)):
                    card = (Mcat1[i]+Mcat2[j]+Mcat3[k])
                    deck.append(card)
print(deck)


#def main():

    #class Word(object):
    #    def __init__(self, name_words, values):
    #        self.name_words = 
    #        self.values = values


    #class WordDeck(list):
    #    def __init__(self):
#
    #     for i in range (0, len(Mcat1)):
    #        for j in range (0, len(Mcat2)):
    #            for k in range (0, len(Mcat3)):
    #                card = Mcat1[i]+Mcat2[j]+Mcat3[k]
    #                deck.append(card)
    #                print(deck)  



#deck = WordDeck()
#for word in deck:
#        print(word)
                
           

    #class ConstructorPhrase(list):
    #    def __init__(self):
    #        pass




#if __name__ == "__main__":
#    main()