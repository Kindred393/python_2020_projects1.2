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