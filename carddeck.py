import random
from card import Card

class CardDeck:
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()

    def __init__(self):
        self._make_deck()

    def _make_deck(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)
    
    @property
    def cards(self):
        return self._cards

    def shuffle(self):
        random.shuffle(self._cards)
    
    # instance methods
    def draw(self):
        return self._cards.pop()

    @classmethod
    def get_ranks(cls):
        return cls.RANKS

    @staticmethod
    def double(x):
        return x * 2

if __name__ == "__main__":
    d1 = CardDeck()  # CardDeck d1 = new CardDeck();
    d2 = CardDeck()
    print(d1)
    d1.shuffle()
    print(d1.cards)
    for i in range(5):
        card = d1.draw()
        print(card)
    print(d1.get_ranks())
    print(CardDeck.get_ranks())

    print(CardDeck.RANKS)
    print(d1.RANKS)