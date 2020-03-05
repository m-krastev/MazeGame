#  Author: CS1527 Course Team
#  Date: 9 January 2020
#  Version: 1.0

from getch1 import *
import sys
import os

#X is the vertical direction
#Y is the horizontal direction

clear = lambda: os.system('cls') #clear screen

class Hero:
    """Hero class with 100 health and 1000 coins by default."""
    def __init__(self):
        """Set the coordinate of the hero in the maze."""
        self._coordX = 0
        self._coordY = 0
        self._health = 100
        self._coins = 1000
        #self._gem=3    #Seems to be irrelevant, commented out.
 
    def set_coord(self,x,y):
        """Sets the coordinates of the hero."""
        self._coordX = x
        self._coordY = y
    
    def return_coords(self):
        """Returns the coordinates of the hero."""
        return self._coordX, self._coordY

    def print_hero_status(self):
        """Prints status of the hero in terms of total HP and gold coins."""
        print("HP:",str(self._health) + "/100","\nCoins:",self._coins,sep="\t")

    def move(self, environment):
        """Move in the maze, it is noted this function may not work in the debug mode."""
        x, y = self.return_coords() #coords that will be changed
        last_coords = (x,y)         #stores last coordinates
        ch2 = getch().upper()
        clear()
        if ch2 == b'H' or ch2 == "A" or ch2 == b'W':
            # the up arrow key was pressed
            print ("up key pressed")
            x-=1            
            if(self.event_check(last_coords, x, y, environment)):
                return True
            else:
                return False

        elif ch2 == b'P' or ch2 == "B" or ch2 == b'S':
            # the down arrow key was pressed
            print("down key pressed")
            x+=1
            if(self.event_check(last_coords, x, y, environment)):
                return True
            else:
                return False

        elif ch2 == b'K' or ch2 == "D" or ch2 == b'A':
            # the left arrow key was pressed
            print("left key pressed")
            y-=1
            if(self.event_check(last_coords, x, y, environment)):
                return True
            else:
                return False

        elif ch2 == b'M' or ch2 == "C" or ch2 == b'D':
            # the right arrow key was pressed
            print("right key pressed")
            y+=1
            if(self.event_check(last_coords, x, y, environment)):
                return True
            else:
                return False

        elif ch2 == b'Z':
            #Print monster coordinates and attributes.
            environment.print_monsters()
            return False
            
        elif ch2 == b'G':
            #Print goblin coordinates and attributes.
            environment.print_goblins()
            return False

        elif ch2 == b'Q':
            #Save the game.
            environment.save_game()
            return False

        elif ch2 == b'R':
            #Load from last checkpoint.
            environment.load_game()
            return False

        elif ch2 == b'L':
            #Shows leaderboard.
            environment.show_leaderboard()
            return False

        elif ch2 == b'Y':
            #Displays hero status.
            self.print_hero_status()
            return False

        elif ch2 == b'I':
            #Prints helpful instructions for the user.
            print(
                "Press W for forward movement.\n"
                "Press S for backward movement.\n"
                "Press A for leftward movement.\n"
                "Press D for rightward movement.\n" 
                "Press Y for Hero status\n"
                "Press I for Instructions.\n"
                "Press O to see the Map.\n"
                "Press Q to Quick Save the game.\n"
                "Press R to reload from last savepoint.\n"
                "Press Z to see the Monsters.\n"
                "Press G to see the Goblins.\n"
                "Press L to see the Leaderboard.\n"
                "Press E to Quick Save and exit the game.\n"
                "*You can also use the arrow keys for movement.\n"
            )
            return False

        elif ch2 == b'O':
            #Displays the map for the user.
            environment.print_environment()
            return False

        elif ch2 == b'E':
            #Exits the game.
            environment.quit_game()
        return False

    '''def move_debug(self, environment):

        """move in the maze, you need to press the enter key after keying in
        direction, and this works in the debug mode"""

        ch2 = sys.stdin.read(1)

        if ch2 == "w":
            # the up arrow key was pressed
            print("up key pressed")
            return True

        elif ch2 == "s":
            # the down arrow key was pressed
            print("down key pressed")
            return True

        elif ch2 == "a":
            # the left arrow key was pressed
            print("left key pressed")
            return True

        elif ch2 == "d":
            # the right arrow key was pressed
            print("right key pressed")
            return True

        return False 
        '''

    def event_check(self, last_coords, x, y, environment):
        current_coord_type = environment.get_coord(x,y)
        if current_coord_type == 1:
            print("You hit a wall! Go back!")
            environment.print_environment()
            self.move(environment)
            return False
        else:
            if current_coord_type == 0:
                environment.set_coord(last_coords[0],last_coords[1],0)
                environment.set_coord(x, y, 2)
                self.set_coord(x,y)
                return True

            elif current_coord_type == 3: #checks whether a monster is encountered
                for monster in environment.monster_list:
                    if monster.return_coords() == (x, y):
                        environment.set_coord(last_coords[0],last_coords[1],0)
                        environment.set_coord(x,y,2)
                        self.set_coord(x,y)
                        monster.fight(self)
                        return True
            elif current_coord_type == 4: #checks whether a goblin is encountered
                for goblin in environment.goblin_list:
                    if goblin.return_coords() == (x, y):
                        environment.set_coord(last_coords[0],last_coords[1],0)
                        environment.set_coord(x, y, 2)
                        self.set_coord(x,y) #saves the position of the hero
                        goblin.interact(self)
                        return True
        return