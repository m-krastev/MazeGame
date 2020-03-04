#  Author: CS1527 Course Team
#  Date: 9 January 2020
#  Version: 1.0

from getch1 import *
from random import random, choice
import rps

class Monster:
    """define your monster class here"""
    def __init__(self, x, y):
        self._coordX = x
        self._coordY = y
        self._flag = False
        return

    def meet_monster(self):
        self._flag = True

    def is_met(self):
        return self._flag

    def return_coords(self):
        return self._coordX, self._coordY

    def interact(self,Hero):
        return


class thiefMonster(Monster):
    def __init__(self,x,y,chance = 0,stolen = 0):
        Monster.__init__(self,x,y)
        self._chance = chance
        self._stolen = stolen
    
    def set_parameters(self, mode):
        self._chance = mode[0][0]
        self._stolen = mode[0][1]
    
    def bio(self):
        print("thief monster at coords (", self._coordX,",",self._coordY,") with attributes (", self._chance, ",", self._stolen,")",sep="")
    
    def interact(self, Hero):
        """fight with monsters"""
        self.meet_monster()
        print("You met a ",end="")
        self.bio()
        if(random() < self._chance):
            Hero._coins -= self._stolen
            print("The monster stole",self._stolen,"coins!")
            return
        else:
            print("You escaped the monster safely!")
            return

class fighterMonster(Monster):
    def __init__(self,x,y,chance = 0,health_reduced = 0):
        Monster.__init__(self,x,y)
        self._chance = chance
        self._health_reduced = health_reduced
    
    def set_parameters(self, mode):
        self._chance = mode[1][0]
        self._health_reduced = mode[1][1]
    
    def bio(self):
        print("fighter monster at coords (", self._coordX,",",self._coordY,") with attributes (", self._chance, ",", self._health_reduced,")",sep="")
    
    def interact(self,Hero):
        """fight with monsters"""
        self.meet_monster()
        print("You met a ",end="")
        self.bio()
        if(random() < self._chance):
                Hero._health -= self._health_reduced
                print("The monster took",self._health_reduced,"HP from you!")
        else:
            print("You escaped the monster safely!")
            return

class gamerMonster(Monster):
    def __init__(self,x,y,health_reduced = 0,stolen = 0):
        Monster.__init__(self,x,y)
        self._health_reduced = health_reduced
        self._gold_stolen = stolen
    
    def set_parameters(self, mode):
        self._health_reduced = mode[2][0]
        self._gold_stolen = mode[2][1]
    
    def bio(self):
        print("gamer monster at coords (", self._coordX,",",self._coordY,") with attributes (", self._health_reduced, ",", self._gold_stolen,")",sep="")
    
    def interact(self,Hero):
        """fight with monsters"""
        self.meet_monster()
        print("You met a ",end="")
        self.bio()
        print("The monster has demanded you play rock-paper-scissors,\nor you will not escape! Press a key to make your move! (R/P/I):")
        playerinput = rps.key_pressed_RPS()
        npcinput = choice(("ROCK","PAPER","SCISSORS"))
        print("You played", playerinput, "while the monster played", npcinput)
        result = rps.rps(playerinput,npcinput)
        while result == 0:
            print("It's a draw! Play again with: ")
            playerinput = rps.key_pressed_RPS()
            npcinput = choice(("ROCK","PAPER","SCISSORS"))
            print("You played", playerinput, "while the monster played", npcinput)
            result = rps.rps(playerinput,npcinput)
        if result == 1:
            print("You won!")
            print("You escaped the monster safely!")
            return
        else:
            Hero._health -= self._health_reduced
            Hero._coins -= self._gold_stolen
            print("The monster has overwhelmed! He stole",self._gold_stolen,"coins and reduced your HP by",self._health_reduced,"points!")
            return