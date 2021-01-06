import random
class Critter(object):
    """this is the class that defines what a critter is"""

    def __init__(self):
        self.health = 100
        self.hunger = 0
        self.height = 0
        self.weight = random.randint(2,6)
        self.name = ""
        self.happy = 50
        self.isAlive = True
    def intro(self):
        print ("hello my name is "+self.getName())

    def hud(self):
        print(self.getName)
        print(self.getHappy)
        health = self.getHealth
        if health > 80:
            print("Health: Great ")
        elif health > 60:
            print("Health: Good")
        elif health > 50:
            print("Health: Fair")
        elif health == 0:
            self.die()
        else:
            print("Health: Poor")
        hunger = self.getHunger()
        if hunger > 40:
            print("Hunger: Starving")
        elif hunger > 20:
            print("Hunger:  Really Hungry")
        elif hunger > 10:
            print("Health: Content")
        elif hunger > 5:
            print("Health: Full")

        else :
            print("Hunger: Hungry")
        if hunger == 100:
            self.die()

        happy = self.getHappy()
        if happy > 50:
            print("Happy: Happy")
        elif happy > 35:
            print("Happy: Content")
        elif happy > 20:
            print("Happy: Sad")
        elif happy > 10:
            print("Happy: Depressed")
        elif happy > 5:
            print("Happy: NO")
    def die (self):
        print("Your pet has died and it's all your fault it had its whole life ahead of them but never again...")
        self.health = 0
        self.isAlive = False




    def getHunger(self, hunger):
        return self.hunger
    def getHealth(self,health):
        return self.health
    def getHeight(self, height):
        return self.height
    def getWeight(self, weight):
        return self.weight
    def getName(self, name):
        return self.name
    def getHappy(self, happy):
        return self.happy





    def setName(self,name):
        if len(name) > 4:
            if (name.contains("uck")) == False:
                self.name = name
    def setHeight(self,height):
        if height < 5 and height >1:
            self.height = height



    def feed(self,food):
        if food == "pizza":
            self.hunger -= 7
        elif food == "cheeseburger":
            self.hunger -= 13
        elif food =="steak":
            self.hunger -= 23
            self.health += 10
        elif food == "corn":
            self.hunger -= 3
            self.health += 1
        elif food == "cheesecake":
            self.hunger-= 100
            self.health-= 5
        else:
            self.hunger -= 5

    def pass_time(self, hours):
        for i in range(hours):
            self.hunger +=2
            if self.hunger < 0:
                self.weight += 1
                self.happy +=10
                self.health -= 5
            if self.hunger > 50:
                self.weight -= 1
                self.happy -=10
                self.health -= 5
            self.happy -= 5

    def play(self,time):
        self.pass_time(self, time)
        self.happy+= 10 *time
        if self.happy >100:
            self.happy = 100
        self.health += 10 * time
        if self.health > 100:
            self.health = 100




def main():
    critter1 = Critter()
    critter1.name = "BillyBobJoe"
    critter2 = Critter()
    critter2.name = "CraaaaazyStan"

    critter1.intro()
    critter2.intro()

def main():
    pet = Critter()
    name = input("what would you like to name your pet")
    pet.setName(name)
    height = int(input("how tall is your pet between 2 and 5"))
    pet.setHeight(height)
    pet.intro()
    pet.hud()
    while pet.isAlive:
        pet.pass_time(1)
        print("what would you like to know")
        print("feed")
        print("play")
        print("nothing")
        response = input()
        if response == "feed":
            food = input("what do you want to feed your pet?")
            pet.feed(food)
        if response == "play":
            time = int(input("how long will you play with your pet?"))
            pet.play(time)
        pet.hud()






main()
