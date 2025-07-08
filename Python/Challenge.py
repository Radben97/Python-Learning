import random as rdm
import sys
import argparse


def guessGame(name="Player"):
    playerWin = 0
    computerWin = 0
    totalGames = 0
    print(f"hi {name},Welcome to my guessing game!\n")
    print("choose a number between 1 and 3\n")
    def game():
        nonlocal playerWin, computerWin, totalGames
        playerGuess = int(input(f"{name}'s Guess:"))
        computerGuess = rdm.choice(range(1,4))
        if playerGuess == computerGuess:
            print(f"you guessed it right!\n The number was {computerGuess}")
            playerWin += 1
            totalGames += 1
            print(f"Total games played: {totalGames}\n")
            print(f"Player wins: {playerWin} \n Computer wins: {computerWin}\n")
            print(f"winPercentage: {playerWin / totalGames: .1%}\n")

        else:
            print(f"Nope you missed it \n The number was {computerGuess}")
            computerWin += 1
            totalGames += 1
            print(f"Total games played: {totalGames}\n")
            print(f"Player wins: {playerWin} \n Computer wins: {computerWin}\n")
            print(f"winPercentage: {playerWin / totalGames: .1%}\n")

        def playAgain():
            print(f"Wanna play again {name}? (y/n): \n")
            inputVal = input().lower()
            if inputVal == "y":
                return game()
            else:
                print(f"Thanks for playing {name}!")
                sys.exit(0)
        playAgain()
    return game()
    
        
    
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A simple guessing game")
    parser.add_argument("-n","--name", help="Enter your name",required=True)
    args = parser.parse_args()
    guessGame(args.name)


        