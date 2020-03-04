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
    playerinput = getch()
    if playerinput == b'R' or playerinput == b'r':
        playerinput = "ROCK"
    elif playerinput == b'P' or playerinput == b'p':
        playerinput = "PAPER"
    elif playerinput == b'I' or playerinput == b'i':
        playerinput = "SCISSORS"
    else:
        playerinput = "invalid key"
    return playerinput