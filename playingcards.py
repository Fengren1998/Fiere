import pydealer

class Dealer:
    def __init__(self):
        self.deck = pydealer.Deck()
        self.shuffle_deck()

    def shuffle_deck(self):
        self.deck.shuffle()

    def deal_deck(self, card):
        hand = self.deck.deal(card)
        return hand
