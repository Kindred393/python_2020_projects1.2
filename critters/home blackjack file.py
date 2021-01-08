#blackJack
#Ethan.Eash
#01/06/21

#import Playing_cards as pc
#import game_functions as gf
#Ethan Eash
# 12\20
#playing cards class

#difficulty settings (define difficulty)
def dificulty():
    question = input("what difficulty would you like Easy, Medium, Hard ")
    #
    if question.startswith("M") or question.startswith("m"):
        difficulty = "Medium"
    elif question.startswith("H") or question.startswith("h"):
        difficulty = "Hard"
    else:
        difficulty = "Easy"
    return dificulty

def open_file(file_name,mode):
    """ open and returns a open file with the given permissions"""
    try:
        file = open("assets/Test_files/"+file_name,mode)
    except IOError as e:
        print("Unable to open the file", file_name, "Ending program. \n", e)
        try:
            file = open("assets/Errors/errors_log.txt","a+")
            time = datetime.now()
            error_time = time.strftime("%M/%D/%Y %H:%M:%S")
            file.writelines(str(e)+str(error_time)+"\n")
            input("\n\nPress the enter key to exit.")
            sys.exit()
        except:
            sys.exit()
    else:
        return file



#print slow text image
def getNumber(question,high,low):
    responce = None
    while responce not in range(low,high):
        slowText(question,0.03)
        responce = input()
        if responce.isnumeric():
            responce = int(responce)
        else:
             slowText("Please enter a number. I can't understand what you put in.",0.01)
    return responce


def slowText(text,amtime):

    """MAKES TYPING EFFECT TEXT"""

    for char in text:
        time.sleep(amtime)
        sys.stdout.write(char)
        sys.stdout.flush()

    time.sleep(0.5)
    print()


#hand =[]
#for i in range(5):
#    suit = random.choice(Card.SUITS)
#    rank = random.choice(Card.RANKS)
#    card = Card(rank, suit)
#    hand.append(card)
#
#for card in hand:
#    print (card)



def ask_yes_no(question):
    response = None
    while response not in ("y", "n"):
        response = int(input(question))
    return response


def ask_numnber(question, low, high):
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

class Player(object):
    def __init__(self, name, score = 0):
        self.name = name
        self.score = Score()
        self.lives = 3

class Score(object):
    def __init__(self):
        self.value = 0
        self.stepvalue = 10

    def add_to(self,itemid):
        for i in range(itemid):
            self.value+=self.stepvalue
            if self.value < 0:
                self.value = 0


if __name__ == "__main__":
    print("you ran this module directly (and did not 'import' it).")
    input("\n\nPress the enter key to exit.")
import random
class Card(object):
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    SUITS = ["♥", "♦", "♣", "♠"]

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        rep = str.format("""
        +--------+
        |{1}{0:>2}     |
        |        | 
        |        | 
        |        |
        |        |
        |        |
        |     {0:2}{1}|
        +--------+
        """,self.rank,self.suit)
        return rep
        return rep

class Hand(object):
    def __init__(self):
        self.cards = []
    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card)
        else:
            rep = "<EMPTY"
        return rep

    def clear(self):
        self.cards = []

    def add(self,card):
        self.cards.append(card)

    def give(self,card,other_hand):
        self.cards.remove(card)
        other_hand.add(card)

class Deck(Hand):
    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank,suit))
    def deal(self,hands,per_hand=1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card,hand)
                else:
                    print("out of cards clearing hands and reShuffling")
                    self.clear()
                    self.populate()
                    self.shuffle()
                    for hand in hands:
                        hand.clear()

class Pos_Card(Card):
    def __init__(self,rank,suit):
        super(Pos_Card, self).__init__(suit,rank)
        self.faceup = True
    def flip(self):
        self.faceup = not self.faceup
    def __str__(self):
        if self.faceup:
            rep = super(Pos_Card, self).__str__()
            return rep
        else:
            rep = """
                +--------+
                |#*#*#*#*|
                |*#*#*#*#| 
                |#*#*#*#*| 
                |*#*#*#*#|
                |#*#*#*#*|
                |*#*#*#*#|
                |#*#*#*#*|
                +--------+
                """
            return rep





if __name__ == "__main__":
    print("You ran this module directly(and did not'import' it).")
    input("\n\nPress the enter key to exit.")
    
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
        
        
    def __str__(self):
        
        print("################################################")
        for card in self.cards:
            print (card)
        rep = "################################################"
        rep+="\n"+self.name
        rep +="\n"+self.total
        return rep

    @property
    def total(self):
        for card in self.cards:
            if not card.value:
                return None

        # add up card values, treat each Ace as 1
        t = 0
        for card in self.cards:
            t +=card.value

        # determine if hand contains an Ace
        has_ace = False
        for card in self.cards:
            if card.value == BJ_Card.ACE_VALUE:
                has_ace = True

        # if hand contains Ace and total is low enough, treat Ace as 11
        if has_ace and t <= 11:
            t+=10 # add only 10 since we've already added 1 for the Ace
        return t

    def is_busted(self):
        return self.total > 21

class BJ_Player(BJ_Hand):

    def bust(self):
        print(self.name, "busts.")
    def lose(self):
        print(self.name, "loses.")
    def win(self):
        print(self.name, "wins.")
    def push(self):
        print(self.name, "pushes.")
    def is_hitting(self):
        response = gf.ask_yes_no("\n" + self.name + ", do you want a hit? (Y/N): "))
        return response == "Y"
class BJ_Dealer(BJ_Hand):
    def is_hitting(self):
        return self.total < 17

     def bust(self):
         print(self.name, "busts.")

    def flip_first_card(self):
        self.cards[0].flip()

class Game(object):
    def __init__(self):
        self.deck = BJ_Deck()
        self.decck.populate()
        self.deck.shuffle()
        self.dealer = BJ_Dealer("Dealer Tim")
        self.players = []
        for name in names:
            player = BJ_Player(name)
            self.players.append(player)

        @property
        def still playing(self):
            sp = []
            for player in self.players:
                if not player.is_busted():
                    sp.append(player)
            return sp
                        

#Testing Area
deck = BJ_Deck()
deck.populate()
deck.shuffle()

card = deck.cards[0]
print(card)
print(card.value)
