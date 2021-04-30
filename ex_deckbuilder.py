def main():
    class Card(object):
        def __init__(self, value, suit):
            self.value = value
            self.suit = suit

        def __repr__(self):
            return "Card"

    class StandardDeck(list):
        def __init__(self):
            super().__init__()
            suits = list(range(4)) 
            values = list(range(13)) 
            [[self.append(Card(i,j)) for j in suits] for i in values]           

    deck = StandardDeck()
    for card in deck:
        print("card", card.value)

if __name__ == "__main__":
    main()
