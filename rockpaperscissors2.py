import getch, sys, time

class go:
    
    def __init__(self):
        self.player = int
        self.choice = str
        self.valid = False
        
    def processInput(self,inp):
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
    go1 = go()
    while go1.valid == False:
        go1.processInput(getch.getch().decode("utf-8"))
    go2 = go()
    while go2.valid == False or go1.player == go2.player:
        go2.processInput(getch.getch().decode("utf-8"))
    return [go1,go2]
        
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

def fullAnalyse(inputs):
    go1 = inputs[0]
    go2 = inputs[1]
    analysis = tryAnalyse(go1,go2)
    if analysis == "retry":
        analysis = tryAnalyse(go2,go1)
    if analysis == "retry":
        sys.exit("Error")
    if analysis == "draw":
        print("It's a draw!")
    else:
        print("Player " + str(analysis) + " wins!")
        
print("""Rock, paper or scissors? Here are the controls:-\n
Player 1: Rock = a, Paper = s, Scissors = d
Player 2: Rock = j, Paper = k, Scissors = l\n
Ready? Press any key...""")
getch.getch()
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("Go!")
inputs = getInputs()
fullAnalyse(inputs)
