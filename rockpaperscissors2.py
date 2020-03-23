import getch, sys

class go:
    player = int
    choice = str
    valid = True
    def __init__(goID,inp):
        if inp in "asdASD":
            goID.player = 1
            if inp in "aA":
                goID.choice = "rock"
            elif inp in "sS":
                goID.choice = "paper"
            else:
                goID.choice = "scissors"
        elif inp in "jklJKL":
            goID.player = 2
            if inp in "jJ":
                goID.choice = "rock"
            elif inp in "kK":
                goID.choice = "paper"
            else:
                goID.choice = "scissors"
        else:
            valid = False

def tryAnalyse(go1,go2):
    if go1.choice == go2.choice:
        return "draw"
    elif go1.choice == "rock" and go2.choice == "paper":
        return go2.player
    elif go1.choice == "rock" and go2.choice == "scissors":
        return go1.player
    elif go1.choice == "paper" and go2.choice == "scissors":
        return go2.player
    else:
        return "retry"

def getInputs():
    go1 = go(getch.getch().decode("utf-8"))
    go2 = go(getch.getch().decode("utf-8"))
    if go1.player == go2.player:
        go2 = go(getch.getch().decode("utf-8"))
    if go1.valid == False:
        go1 = go(getch.getch().decode("utf-8"))
    if go2.valid == False:
        go2 = go(getch.getch().decode("utf-8"))
    # after five seconds notify that still waiting for an input
        
def fullAnalyse():
    analysis = analyseDraw(go1,go2)
    if analysis == "retry":
        analysis = analyseDraw(go2,go1)
    if analysis == "draw":
        print("It's a draw!")
    else:
        print("Player",analysis,"wins!")

print("Rock, paper or scissors?\n
      Player 1: Rock = a, Paper = s, Scissors = d\n
      Player 2: Rock = j, Paper = k, Scissors = l")
getInputs()
fullAnalyse()
