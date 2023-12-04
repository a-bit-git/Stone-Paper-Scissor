print(""" >>>  STONE-PAPER-SCISSOR  <<<
      >>> GAME RULES <<<

Player 1 : Computer
Player 2 : You
(a) Enter '1' for 'Stone'
(b) Enter '2' for 'Paper'
(c) Enter '3' for 'Scissor'

Stone over Scissor
Paper over Stone
Scissor over Paper
Same Entry get Tie
""")
import random
def Game():
    computer=random.randint(1,3)
    if (computer==1):
        computer="Stone"
    elif (computer==2):
        computer="Paper"
    else:
        computer="Scissor"
    while True:
        you = input("Enter a term out of (1), (2) or (3) only = ")
        if (you=="1"):
            you="Stone"
            break
        elif (you=="2"):
            you="Paper"
            break
        elif (you=="3"):
            you="Scissor"
            break
        else:
            print("Invalid entry")
    print("Computer Entry :",computer)
    print("Your Entry :",you)
    if((computer=="Stone" and you=="Paper")or(computer=="Paper" and you=="Scissor")or(computer=="Scissor" and you=="Stone")):
        print("You Won, Computer Loss !!!")
    elif(computer==you):
        print("It's Tie !!!")
    else:
        print("You Loss, Computer Won !!!")
Game()