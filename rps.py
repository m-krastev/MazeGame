#Rock Paper Scissors game
#R - ROCK, P - PAPER, I - SCISSORS
#0 for draw
#1 for first player win
#-1 for second player win

from getch1 import *
from random import choice

def rps(player1Input, player2Input):
    '''Calculates results of a game of Rock-Paper-Scissors, assumes correct values'''
    if player1Input == player2Input:
        return 0
    else:
        if player1Input == "ROCK" and player2Input == "SCISSORS":
            return 1
        if player1Input == "PAPER" and player2Input == "ROCK":
            return 1
        if player1Input == "SCISSORS" and player2Input == "PAPER":
            return 1
    return -1

def key_pressed_RPS():
    """Normalizes input for a game of Rock-Paper-Scissors."""
    playerinput = getch().upper()
    if playerinput == b'R':
        playerinput = "ROCK"
    elif playerinput == b'P':
        playerinput = "PAPER"
    elif playerinput == b'I':
        playerinput = "SCISSORS"
    else:
        playerinput = choice(("ROCK","PAPER","SCISSORS"))
    return playerinput