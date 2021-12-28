import random
try:
    def randNum(num1):
        num = random.randint(1, 3)
        output = "Invalid Input"
        choice = "none"
        computer = "none"
        if num == num1:
            output = "Tie"
            if num == 1:
                choice = computer = "rock"
            if num == 2:
                choice = computer = "paper"
            if num == 3:
                choice = computer = "scissors"
        elif num == 1 and num1 == 2:
            output = "You Win"
            choice = "paper"
            computer = "rock"
        elif num == 1 and num1 == 3:
            output = "You Lose"
            choice = "scissors"
            computer = "rock"
        elif num == 2 and num1 == 1:
            output = "You Lose"
            choice = "rock"
            computer = "paper"
        elif num == 2 and num1 == 3:
            output = "You Win"
            choice = "scissors"
            computer = "paper"
        elif num == 3 and num1 == 1:
            output = "You Win"
            choice = "rock"
            computer = "scissors"
        elif num == 3 and num1 == 2:
            output = "You Lose"
            choice = "paper"
            computer = "scissors"
        if output == "Invalid Input":
            print(output)
        else:
            print(output)
            print("You chose " + choice + " and the computer chose " + computer + "!")
    randNum(int(input("Type out 1 for rock, 2 for paper, 3 for scissors: ")))
except ValueError:
    print("Invalid Input")