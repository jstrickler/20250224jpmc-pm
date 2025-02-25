from carddeck import CardDeck
from card import Card

class GameMixin:
    def start(self):
        print("starting game")

class JokerDeck(GameMixin, CardDeck):
    def _make_deck(self):
        super()._make_deck()
        for joker_number in 1, 2:
            joker = Card(f"JOKER-{joker_number}", "JOKER")
            self._cards.append(joker)

if __name__ == "__main__":
    j = JokerDeck()
    j.shuffle()
    for i in range(5):
        print(j.draw())
    j.start()
    print(JokerDeck.mro())