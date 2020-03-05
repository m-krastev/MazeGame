from hero import Hero
from monster import *
from goblin import *
from getch1 import *
from maze_gen_recursive import make_maze_recursion
from copy import deepcopy
from random import randint
from rps import rps
from colorama import init, Fore
import pickle

MAZE_DIMENSION_X = 17
MAZE_DIMENSION_Y = 17

DIVIDERS = "=========================================="

WALL_CHAR = "#"      #"\u25a0"
SPACE_CHAR = "-"     #" "
HERO_CHAR = "H"
MONSTER_CHAR = u"\u001b[31m"+"M"+u"\u001b[0m" #RED MONSTERS
GOBLIN_CHAR = u"\u001b[32m"+"G"+u"\u001b[0m"  #GREEN GOBLINS

class _Environment:
    """Environment includes the Maze, the Monsters, and the Goblins."""
    def __init__(self, maze):
        self._environment = deepcopy(maze)
        self.monster_list = []
        self.goblin_list = []
        self.spawn_monsters_goblins()

    def set_coord(self, x, y, val):
        """Assigns a type to the cell, denoted by the coordinates."""
        self._environment[x][y] = val

    def get_coord(self, x, y):
        """Returns the type of the cell, denoted by the coordinates."""
        return self._environment[x][y]
    
    def spawn_monsters_goblins(self):
        """Spawns monsters and goblins into the maze."""
        #Spawns the monsters.
        for i in range(5):
            while True:
                x = randint(2,MAZE_DIMENSION_X-2)
                y = randint(2,MAZE_DIMENSION_Y-2)
                if not self.get_coord(x,y):
                    self.set_coord(x,y,3)
                    type_ = randint(0,2)
                    if type_ == 0:
                        self.monster_list.append(thiefMonster(x,y))
                    elif type_ == 1:
                        self.monster_list.append(fighterMonster(x,y))
                    else:
                        self.monster_list.append(gamerMonster(x,y))
                    break
        #Spawns the goblins.
        for i in range(5):
            while True:
                x = randint(2,MAZE_DIMENSION_X-2)
                y = randint(2,MAZE_DIMENSION_Y-2)
                if not self.get_coord(x,y):
                    self.set_coord(x,y,4)
                    type_ = randint(0,2)
                    if type_ == 0:
                        self.goblin_list.append(wealthGoblin(x,y))
                    elif type_ == 1:
                        self.goblin_list.append(healthGoblin(x,y))
                    else:
                        self.goblin_list.append(gamerGoblin(x,y))
                    break
        return

    def print_environment(self):
        """Print out the environment (the maze) in the terminal."""
        print(DIVIDERS)
        for row in self._environment:
            row_str = str(row)
            row_str = row_str.replace("0", SPACE_CHAR)      # replace the space character
            row_str = row_str.replace("1", WALL_CHAR)       # replace the wall character
            row_str = row_str.replace("2", HERO_CHAR)       # replace the hero character
            row_str = row_str.replace("3", MONSTER_CHAR)    # replace the monster char
            row_str = row_str.replace("4", GOBLIN_CHAR)     # replace the goblin char
            print("".join(row_str)) #print("".join(row_str).replace(",",""))

    def print_monsters(self):
        """Returns a list of all the monsters in the maze."""
        for monster in self.monster_list:
            monster.bio()
            
    def print_goblins(self):
        """Returns a list of all the goblins in the maze."""
        for goblin in self.goblin_list:
            goblin.bio()
    #The following functions exist for the sake of access inside the Hero controls.
    def save_game(self, game):
        try:
            myGame.save_game()
        except Exception:
            pass
        return

    def load_game(self):
        try:
            myGame.load_game()
        except Exception:
            pass
        return

    def show_leaderboard(self):
        try:
            myGame.show_leaderboard()
        except Exception:
            pass
        return

    def quit_game(self):
        try:
            myGame.quit_game()
        except Exception:
            pass
        return

class Game:
    def __init__(self):
        self.myHero = Hero()
        self.maze = make_maze_recursion(MAZE_DIMENSION_X, MAZE_DIMENSION_Y)
        self.MyEnvironment = _Environment(self.maze)  # initial environment is the maze itself
        self._count = 0
        self._difficulty = 0
        
    def set_difficulty(self, difficulty):
        """Sets the difficulty of the game."""
        for monster in self.MyEnvironment.monster_list:
            monster.set_parameters(difficulty)
        for goblin in self.MyEnvironment.goblin_list:
            goblin.set_parameters(difficulty)

    def new_game(self):
        """Initiates a new game of Maze."""

        print("Game start!\n")

        self._difficulty = input("Difficulties:\n"
            "Easy (0): Monsters are weak and have low chance of attacking you, low risks. Goblins are generous and reliable.\n"
            "Normal (1): Monsters are dangerous and can attack you, medium risk. Goblins are more generous, but less often.\n"
            "Hard (2): Monsters are highly aggressive and will harm you, high risk. Goblins are wealthy, but will seldom show you kindness.\n"
            "Monster (3): Successive monster encounters can kill you. Goblins will reward you handsomely if they take a liking in you, but this will probably not happen.\n"
            "Choose your mode: "
            )

        self.set_difficulty(int(self._difficulty))
    
        #Sets the initial position of the hero.
        while True:
            x = randint(2,MAZE_DIMENSION_X-2)
            y = randint(2,MAZE_DIMENSION_Y-2)
            if not self.MyEnvironment.get_coord(x,y):
                self.MyEnvironment.set_coord(x,y,2)
                self.myHero.set_coord(x,y)
                break
        #Informs the player of the positions of the mobs in the game.
        self.MyEnvironment.print_monsters()
        self.MyEnvironment.print_goblins()

    def save_game(self):
        """Saves the game to a pre-determined file."""
        print("Saving game... ")
        with open("game_save.dat","wb") as file:
            pickle.dump([self.myHero,self.MyEnvironment,self._count,self._difficulty],file)
        return

    def load_game(self):
        """Loads the game from a pre-determined file. File must NOT be empty."""
        print("Loading game... ")
        with open("game_save.dat","rb") as file:
            self.myHero,self.MyEnvironment,self._Count,self._difficulty = pickle.load(file)
        return
    
    def quit_game(self):
        """"Stops the program."""
        self.save_game()
        print("Quitting the game...")
        quit()

    def win_check(self):
        """Determines whether the player has reached a winning or losing condition."""
        if self.myHero._health < 1:
            print("Game Over!\nThe Hero has died!\n")
            return True

        flag = 0

        print("Monsters visited:\n[",end="")
        for monster in self.MyEnvironment.monster_list:
            if monster.is_met():
                flag += 1
                mon_x,mon_y = monster.return_coords()
                self.MyEnvironment.set_coord(mon_x,mon_y,3) #Reassigns monster coordinates, this is done because of poorly designed code 
                print("1",end="; ")                         #that would otherwise move the position of the monster with the hero.
            else:
                print("0",end="; ")
        print(flag,"/5]",sep="")

        if flag == 5:
            #If game is beaten, prompts the user to record their name in the Hall of Fame for the difficulty.
            print("Game beaten! Congratulations!")
            userinput = input("Would you like to record your achievement in the leaderboard? Type \"yes\" to proceed... ")
            if userinput == "yes":
                self.save_leaderboard()
                self.show_leaderboard()
            return True
        return False

    def show_leaderboard(self):
        """Shows the leaderboard for the given difficulty."""
        with open("leaderboards/leaderboard_{}.dat".format(self._difficulty),"r") as file:
            print(DIVIDERS)
            print("Rank","Name", "Score", sep="\t")
            for index, line in enumerate(file):
                line = line.strip()
                score, name = line.split(sep=",")
                print(index+1, name.strip(), score, sep="\t")
                if index == 9:
                    break
        return

    def save_leaderboard(self):
        """Saves the leaderboard for the given difficulty."""
        inserted = False
        name = input("Name yourself adventurer, your deeds will be passed down in history: ")
        with open("leaderboards/leaderboard_{}.dat".format(self._difficulty),"r+") as file:
            lb = file.readlines()
            for index, line in enumerate(lb):
                if self.myHero._coins > int(line.split(sep=",",maxsplit = 1)[0]):
                    lb.insert(index,",".join([str(self.myHero._coins),name+"\n"]))
                    inserted = True
                    break
            if not inserted:
                lb.append(",".join(["\n"+str(self.myHero._coins),name]))
            file.seek(0)        #<---- Function will ABSOLUTELY NOT work without these, DON'T EVER TOUCH THIS WHOLE FUNCTION
            file.truncate(0)
            file.write("".join(lb))
        return

    def play(self):
        """Main function for playing the game."""
        #First prompts the user whether they want to load from the last saved file or start a new game.
        print("Hello World! Press L to load from your last game or N to start a New Game... ")

        start = getch()
        if start == b"L" or start == b'l':
            self.load_game()
        if start == b"N" or start == b'n':
            self.new_game()

        while True:
            if self.myHero.move(self.MyEnvironment):
                self.MyEnvironment.print_environment()
                self._count += 1
                print(DIVIDERS, self._count)
                self.myHero._health -= 1   #Hero's health reduces.
                self.myHero.print_hero_status()
                if self.win_check():
                    break

if __name__ == "__main__":
    myGame = Game()
    myGame.play()
