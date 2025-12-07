from random import randint

def player_guesses():
    """
    Mode 1: The computer picks a number and the player guesses it.
    """
    print("I am thinking of a number between 1 and 10...")
    secret_number = randint(1, 10)
    attempts = 0

    while True:
        guess = int(input("Your guess: "))
        attempts += 1

        if guess > secret_number:
            print("My number is smaller.")
        elif guess < secret_number:
            print("My number is larger.")
        else:
            print(f"Congratulations! You guessed my number in {attempts} attempts.")
            break


def computer_guesses():
    """
    Mode 2: The player picks a number and the computer guesses it.
    """
    print("Think of a number between 1 and 10, and I will try to guess it!")
    
    low = 1
    high = 10
    attempts = 0

    while True:
        computer_guess = (low + high) // 2
        attempts += 1

        print(f"My guess is {computer_guess}")
        print("Is your number:")
        print("  '+'  greater than my guess")
        print("  '-'  less than my guess")
        print("  '='  equal to my guess")

        response = input("Your answer: ")

        if response == "=":
            print(f"I guessed your number in {attempts} attempts!")
            break
        elif response == "+":
            low = computer_guess + 1
        elif response == "-":
            high = computer_guess - 1
        else:
            print("Invalid input. Please enter '+', '-', or '='.")


def main():
    print("Welcome to the Number Guessing Game!")
    print("Choose a mode:")
    print("  1 :You guess the number")
    print("  2 :I guess your number")

    choice = input("Enter 1 or 2: ")

    if choice == "1":
        player_guesses()
    elif choice == "2":
        computer_guesses()
    else:
        print("Invalid choice. Please restart the game.")

