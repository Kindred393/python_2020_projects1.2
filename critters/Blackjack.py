#blackJack
#Ethan.Eash
#01/06/21
import Playing_cards as pc
import game_functions as gf

class BJ_Cards(pc.Pos_Card):
    ACE_VALUE = 1
    @property
    def value(self):
        if self.faceup:
            V = BJ_Cards.RANKS.index((self.rank))+1
            if V > 10:
                V = 10
        else:
            V = None
        return V


class BJ_Deck(pc.Deck):
    def populate(self):
        for suit in BJ_Cards.SUITS:
            for rank in pc.Card.RANKS:
                self.add(BJ_Cards(rank,suit))

class BJ_Hand(pc.hand):
    def __init__(name):
        super(BJ_Hand, self).__init__()
        self.name = name



#Testing Area
deck = BJ_Deck()
deck.populate()
deck.shuffle()

card = deck.cards[0]
print(card)
print(card.value)