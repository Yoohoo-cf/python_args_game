from rps import rps
from guess_number import guess_number
import sys

def play_game(name='PlayerOne'):
    welcome_back = False

    while True:
        if welcome_back == True:
            print(f"{name}, welcome back to the Arcade menu! ☺️\n")

        playerchoice = input(
            f"\nPlease choose a game:\n1 = Rock Paper Scissors\n2 = Guess my number\n\nOr press \"x\" to exit the Arcade\n\n"
        )

        if playerchoice not in ["1", "2", "x"]:
            print(f"\n{name}, please choose 1, 2 or x")
            return play_game(name)

        
        if playerchoice == "1":
            rock_paper_scissors = rps(name)
            rock_paper_scissors()
        elif playerchoice == "2":
            guess_number_game = guess_number(name)
            guess_number_game()
        else:
            print(f"\nSee you next time!\n")
            sys.exit(f"Bye {name}!👋")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the game."
    )

    args = parser.parse_args()

    
    print(f"\n{args.name}, welcome to the Arcade! 🤗")
    play_game(args.name)       

