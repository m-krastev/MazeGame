from getch1 import *
from random import random, choice
import rps

class Goblin:
    """Parent goblin class."""
    def __init__(self,x,y):
        self._coordX = x
        self._coordY = y
        return
    
    def return_coords(self):
        """Returns the coordinates of the goblin."""
        return self._coordX, self._coordY

class wealthGoblin(Goblin):
    """Wealth goblin will reward the hero with a certain probability."""
    def __init__(self,x,y):
        Goblin.__init__(self, x ,y)
        self._chance = 0
        self._gift = 0
    
    def set_parameters(self, mode):
        """Sets parameters according to a pre-defined array in playgame.py"""
        difficulty = [[0.33,150], [0.25,300], [0.15,500], [0.10,1200]]
        self._chance = difficulty[mode][0]
        self._gift = difficulty[mode][1]

    def bio(self):
        """Prints a short description of the goblins."""
        print("wealth goblin at coords (", self._coordX,",",self._coordY,") with attributes (", self._chance, ",", self._gift,")",sep="")

    def interact(self,Hero):
        """Establishes the interaction that will happen when the Hero meets the Goblin."""
        print("You met a ",end="")
        self.bio()
        if(random() < self._chance):
            Hero._coins += self._gift
            print("The goblin has gifted you with",self._gift,"coins!")
            return
        print("You have parted ways with the goblin...")
        return
        


class healthGoblin(Goblin):
    """Health goblin will restore the Hero's HP with a certain probability"""
    def __init__(self,x,y):
        Goblin.__init__(self, x ,y)
        self._chance = 0
        self._health_restored = 0

    def set_parameters(self, mode):
        """Sets parameters according to a pre-defined array in playgame.py"""
        difficulty = [[0.40,40],[0.25,50],[0.20,40],[0.10,100]]
        self._chance = difficulty[mode][0]
        self._health_restored = difficulty[mode][1]

    def bio(self):
        """Prints a short description of the goblins."""
        print("health goblin at coords (", self._coordX,",",self._coordY,") with attributes (", self._chance, ",", self._health_restored,")",sep="")
    
    def interact(self,Hero):
        """Establishes the interaction that will happen when the Hero meets the Goblin."""
        print("You met a ",end="")
        self.bio()
        if(random() < self._chance):
            Hero._health += self._health_restored
            print("The goblin healed",self._health_restored,"HP for you!")
            return
        print("You have parted ways with the goblin...")
        return


class gamerGoblin(Goblin):
    """Gamer goblin will play a game with the Hero and if the Hero wins, he will be rewarded by the goblin with more HP and coins. Otherwise, Hero will not receive anything."""
    def __init__(self,x,y):
        Goblin.__init__(self, x, y)
        self._health_restored = 0
        self._gift = 0

    def set_parameters(self, mode):
        """Sets parameters according to a pre-defined array in playgame.py"""
        difficulty = [[180,50],[400,60],[500,70],[800,80]]
        self._gift = difficulty[mode][0]
        self._health_restored = difficulty[mode][1]

    def bio(self):
        """Prints a short description of the goblins."""
        print("gamer goblin at coords (", self._coordX,",",self._coordY,") with attributes (", self._gift, ",", self._health_restored,")",sep="")
    
    def interact(self,Hero):
        """Establishes the interaction that will happen when the Hero meets the Goblin."""
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
            Hero._health += self._health_restored
            Hero._coins += self._gift
            print("You won! The goblin wants to reward you! He gave you",self._gift,"coins and restored your HP by",self._health_restored,"points!")
            return
        else:
            print("The goblin won! You will not be rewarded.")
        return