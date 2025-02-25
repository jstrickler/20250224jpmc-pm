class Card: # inherits from 'object'
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    @property
    def rank(self): # getter property
        return self._rank
    # rank = property(rank)
    
    @rank.setter
    def rank(self, value):
        self._rank = value


    @property
    def suit(self): # getter property
        return self._suit.title()

    @suit.setter
    def suit(self, value):
        if isinstance(value, str):
            self._suit = value
        else:
            raise TypeError("suit must be a string")
        
    def __str__(self):   # str(obj)
        return f"{self.rank}-{self.suit}"
    
    def __repr__(self):
        return f"Card('{self.rank}', '{self.suit}')"


if __name__ == "__main__":
    c = Card("3", "CLUBS")
    print(c)
    print(c.rank, c.suit)
 #   print(c.get_rank())
    c.rank = '4'
    print(c)
    print(repr(c)) #  Card('4', 'Clubs')
    print(f"{c = }")
    
