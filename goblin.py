#  Author: CS1527 Course Team
#  Date: 9 January 2020
#  Version: 1.0

from getch1 import *
from random import random, choice
import rps

class Goblin:
    def __init__(self,x,y):
        self._coordX = x
        self._coordY = y
        return

    def meet_goblin(self):
        pass
    
    def return_coords(self):
        return self._coordX, self._coordY
    
    def bio(self):
        print("default goblin")

    def interact(self, Hero):
        return

class wealthGoblin(Goblin):
    def __init__(self,x,y,chance = 0.25,gift = 40):
        Goblin.__init__(self, x ,y)
        self._chance = chance
        self._gift = gift
    
    def set_parameters(self, mode):
        self._chance = mode[3][0]
        self._gift = mode[3][1]

    def bio(self):
        print("wealth goblin at coords (", self._coordX,",",self._coordY,") with attributes (", self._chance, ",", self._gift,")",sep="")

    def interact(self,Hero):
        self.meet_goblin()
        print("You met a ",end="")
        self.bio()
        if(random() < self._chance):
            Hero._coins += self._gift
            print("The goblin has gifted you with",self._gift,"coins!")
            return
        print("You have parted ways with the goblin...")
        del self
        return
        


class healthGoblin(Goblin):
    def __init__(self,x,y,chance = 0.5,health_restored = 20):
        Goblin.__init__(self, x ,y)
        self._chance = chance
        self._health_restored = health_restored

    def set_parameters(self, mode):
        self._chance = mode[4][0]
        self._health_restored = mode[4][1]

    def bio(self):
        print("health goblin at coords (", self._coordX,",",self._coordY,") with attributes (", self._chance, ",", self._health_restored,")",sep="")
    
    def interact(self,Hero):
        self.meet_goblin()
        print("You met a ",end="")
        self.bio()
        if(random() < self._chance):
            Hero._health += self._health_restored
            print("The goblin healed",self._health_restored,"HP for you!")
            return
        print("You have parted ways with the goblin...")
        del self
        return


class gamerGoblin(Goblin):
    def __init__(self,x,y,health_restored = 30, gift = 150):
        Goblin.__init__(self, x ,y)
        self._health_restored = health_restored
        self._gift = gift

    def set_parameters(self, mode):
        self._gift = mode[5][1]
        self._health_restored = mode[5][0]

    def bio(self):
        print("gamer goblin at coords (", self._coordX,",",self._coordY,") with attributes (", self._gift, ",", self._health_restored,")",sep="")
    
    def interact(self,Hero):
        self.meet_goblin()
        print("You met a ",end="")
        self.bio()
        print("The goblin insists you play rock-paper-scissors\nwith him so that he will reward you! Press a key to make your move! (R/P/I):")
        playerinput = rps.key_pressed_RPS()
        npcinput = choice(("ROCK","PAPER","SCISSORS"))
        print("You played", playerinput, "while the goblin played", npcinput)
        result = rps.rps(playerinput,npcinput)
        while result == 0:
            print("It's a draw! Play again with: ")
            playerinput = rps.key_pressed_RPS()
            npcinput = choice(("ROCK","PAPER","SCISSORS"))
            print("You played", playerinput, "while the goblin played", npcinput)
            result = rps.rps(playerinput,npcinput)
        if result == 1:
            print("You won!")
            Hero._health += self._health_restored
            Hero._coins += self._gift
            print("The goblin wants to reward you! He gave you",self._gift,"coins and restored your HP by",self._health_restored,"points!")
            return
        else:
            print("The goblin won! You will not be rewarded.")
        del self
        return