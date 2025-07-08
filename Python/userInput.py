import sys
import random


value = str(input("enter your name: "))
PlayerChoice = int(input("1 for rock\n2 for paper\n 3 for scissors: "))
print(value)
if PlayerChoice < 1 or PlayerChoice > 3:
    sys.exit("You must choose 1,2 or 3")
computerChoice = int(random.choice("123"))

player = str(PlayerChoice)
computer = str(computerChoice)

print("you chose " + player + ".")
print("I chose " + computer + ".")

if PlayerChoice == 1 and computerChoice == 2:
    sys.exit("I win")
if PlayerChoice == 1 and computerChoice == 3:
    sys.exit("you win")
if PlayerChoice == 2 and computerChoice == 1:
    sys.exit("you win")
if PlayerChoice == 2 and computerChoice == 3: # use elif instead of ifs
    sys.exit("I win")
if PlayerChoice == 3 and computerChoice == 1:
    sys.exit("I win")
if PlayerChoice == 3 and computerChoice == 2:
    sys.exit("you win")
else:
    sys.exit("tie")


