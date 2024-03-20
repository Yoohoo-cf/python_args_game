import sys
import random

def guess_number(name='PlayerOne'):
    game_count = 0
    player_wins = 0

    def play_guess():
        nonlocal name
        nonlocal player_wins

        playerchoice = input(
            f"\n{name}, guess which number I am thinking of...1, 2 or 3? \n\n")

        if playerchoice not in ["1", "2", "3"]:
            print(f"\n{name}, please enter 1, 2 or 3.")
            return play_guess()

        player = int(playerchoice)

        think_number_choice = random.choice("123")

        think = int(think_number_choice)

        print(
            f"\n{name}, you chose {player}."
        )
        print(
            f"\nI was thinking about the number {think}.\n"
        )

        def decide_winner(player, think):
            nonlocal name
            nonlocal player_wins

            if player == think:
                player_wins += 1
                return f"\n🎉🎉🎉 {name}, you win!"
            else:
                return f"\nSorry, {name}...😕 better luck next time"

        guess_result = decide_winner(player, think)
        print(guess_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame count: {game_count}")
        print(f"\n{name}'s wins: {player_wins}")
        if player_wins > 0:
            wins_rate = player_wins / game_count
            print(f"\nYour winning percentage: {wins_rate:.2%}")

        print(f"\nPlay again, {name}?")

        while True:
            playagain = input("\nY for Yes or \nQ to Quit\n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_guess()
        else:
            print("\n")
            print("Thank you for playing!\n")
            if __name__ == "__main__":
                sys.exit(f"Bye {name}! 👋👋👋")
            else:
                return

    return play_guess()


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

    guess_number_game = guess_number(args.name)
    guess_number_game()






