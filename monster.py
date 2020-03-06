from getch1 import *
from random import random, choice
import rps

class Monster:
    """Parent monster class."""
    def __init__(self, x, y):
        self._coordX = x
        self._coordY = y
        self._flag = False
        return

    def meet_monster(self):
        """Meet monster. Turns the flag on."""
        self._flag = True

    def is_met(self):
        """Returns the flag of the monster."""
        return self._flag

    def return_coords(self):
        """Returns the coordinates of the monster."""
        return self._coordX, self._coordY

class thiefMonster(Monster):
    """Thief monster will steal coins from the Hero with a predefined probability."""
    def __init__(self,x,y):
        Monster.__init__(self,x,y)
        self._chance = 0
        self._stolen = 0
    
    def set_parameters(self, mode):
        """Sets parameters according to a pre-defined array in playgame.py"""
        difficulty = [[0.25, 100], [0.33,200], [0.50,300], [0.75,400]] #EASY, NORMAL, HARD, MONSTER
        self._chance = difficulty[mode][0]
        self._stolen = difficulty[mode][1]
    
    def bio(self):
        """Prints a short description of the monster."""
        print("thief monster at coords (", self._coordX,",",self._coordY,") with attributes (", self._chance, ",", self._stolen,")",sep="")
    
    def fight(self, Hero):
        """Establishes the interaction that will happen between the Hero and the Monster."""
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
    """Fighter monster will reduce the Hero's health with a predefined probability."""
    def __init__(self,x,y):
        Monster.__init__(self,x,y)
        self._chance = 0
        self._health_reduced = 0
    
    def set_parameters(self, mode):
        """Sets parameters according to a pre-defined array in playgame.py"""
        difficulty = [[0.10,25],[0.25,30],[0.50,35],[0.80,40]] #EASY, NORMAL, HARD, MONSTER
        self._chance = difficulty[mode][0]
        self._health_reduced = difficulty[mode][1]
    
    def bio(self):
        """Prints a short description of the monster."""
        print("fighter monster at coords (", self._coordX,",",self._coordY,") with attributes (", self._chance, ",", self._health_reduced,")",sep="")
    
    def fight(self,Hero):
        """Establishes the interaction that will happen between the Hero and the Monster."""
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
    """Gamer monster will play a game with the hero and will not harm the hero if the hero wins. Otherwise, it will steal coins and reduce Hero's health."""
    def __init__(self,x,y):
        Monster.__init__(self,x,y)
        self._health_reduced = 0
        self._gold_stolen = 0
    
    def set_parameters(self, mode):
        """Sets parameters according to a pre-defined array in playgame.py"""
        difficulty = [[30,100],[40,200],[50,400],[60,800]]
        self._health_reduced = difficulty[mode][0]
        self._gold_stolen = difficulty[mode][1]
    
    def bio(self):
        """Prints a short description of the monster."""
        print("gamer monster at coords (", self._coordX,",",self._coordY,") with attributes (", self._health_reduced, ",", self._gold_stolen,")",sep="")
    
    def fight(self,Hero):
        """Establishes the interaction that will happen between the Hero and the Monster."""
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
            print("You won and escaped the monster safely!")
            return
        else:
            Hero._health -= self._health_reduced
            Hero._coins -= self._gold_stolen
            print("The monster has overwhelmed! He stole",self._gold_stolen,"coins and reduced your HP by",self._health_reduced,"points!")
            return