###############################################################
# Simple implementation of a two-player Rock, Paper, Scissors #
# game, using the getch module for keyboard inputs.           #
###############################################################

import getch, sys, time

class go:
# Defines an object 'go' which contains a single player's
# identity and choice of rock, paper or scissors.
    
    def __init__(self):
        self.player = int
        self.choice = str
        self.valid = False # has player given a valid input?

    def processInput(self,inp):
    # receives character inp from getch, translates into
    # player's identity and rock, paper or scissors
    
        if inp in "asdASD":
            self.player = 1
            if inp in "aA":
                self.choice = "rock"
            elif inp in "sS":
                self.choice = "paper"
            else:
                self.choice = "scissors"
            self.valid = True
            
        if inp in "jklJKL":
            self.player = 2
            if inp in "jJ":
                self.choice = "rock"
            elif inp in "kK":
                self.choice = "paper"
            else:
                self.choice = "scissors"
            self.valid = True

        
def getInputs():
# Keep taking a character from getch until a valid one
# is entered, guards against accidental keypresses

    go1 = go() # first input received
    while go1.valid == False:
        go1.processInput(getch.getch().decode("utf-8"))

    go2 = go() # second input received
    
    # if two characters are taken from the same player,
    # second one is replaced until the other player has
    # entered a valid one
    while go2.valid == False or go1.player == go2.player:
        go2.processInput(getch.getch().decode("utf-8"))
    return [go1,go2]


def fullAnalyse(inputs):
# Performs complete analysis to determine who has won

    go1 = inputs[0]
    go2 = inputs[1]
    analysis = tryAnalyse(go1,go2)

    # If tryAnalyse hasn't found a winner, swap inputs to
    # try other possibilities
    if analysis == "retry":
        analysis = tryAnalyse(go2,go1)
    if analysis == "retry":
        sys.exit("Error")

    # Print outcome to stdout
    if analysis == "draw":
        print("It's a draw!")
    else:
        print("Player " + str(analysis) + " wins!")


def tryAnalyse(goA,goB):
# Analysis of half of the possibilities dictating who has won

    if goA.choice == goB.choice:
        return "draw"
    elif goA.choice == "rock" and goB.choice == "paper":
        return goB.player
    elif goA.choice == "rock" and goB.choice == "scissors":
        return goA.player
    elif goA.choice == "paper" and goB.choice == "scissors":
        return goB.player
    else:
        return "retry"

        
print("""Rock, paper or scissors? Here are the controls:-\n
Player 1: Rock = a, Paper = s, Scissors = d
Player 2: Rock = j, Paper = k, Scissors = l\n
Ready? Press any key...""")
getch.getch() # wait for any keypress
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("Go!")
inputs = getInputs() # take players' inputs
fullAnalyse(inputs) # analyse and print winner
