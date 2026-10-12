
import random


def play_game():
    # Generate a random number between 1 and 100.
    secret_number = random.randint(1, 100)
    total_attempts = 7
    attempts_left = total_attempts

    print("\n===== NUMBER GUESSING GAME =====")
    print("I have selected a number between 1 and 100.")
    print(f"You have {total_attempts} attempts to guess it.")

    while attempts_left > 0:
        try:
            guess = int(input("\nEnter your guess: "))

            # Validate the guess range.
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

        except ValueError:
            print("Invalid input! Please enter a whole number.")
            continue

        # Count only valid guesses.
        attempts_left -= 1

        if guess == secret_number:
            print("Congratulations! You guessed correctly!")
            print(f"Attempts used: {total_attempts - attempts_left}")
            print(f"Attempts left: {attempts_left}")
            return

        elif guess > secret_number:
            print("Too High! Try a smaller number.")

        else:
            print("Too Low! Try a bigger number.")

        print(f"Attempts left: {attempts_left}")

    print("\nGame over! You have used all your attempts.")
    print(f"The secret number was {secret_number}.")


def main():
    # Allow the player to start another round.
    while True:
        play_game()

        choice = input("\nPlay again? (yes/no): ").strip().lower()

        if choice not in ("yes", "y"):
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
