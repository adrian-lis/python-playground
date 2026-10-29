import random

while True:
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Number Guesser")

    while True:
        try:
            guess = int(input("Guess the number (1-100): "))
        except ValueError:
            print("Invalid input. Enter a whole number.")
            continue

        if guess < 1 or guess > 100:
            print("Number must be between 1 and 100.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Higher!")
        elif guess > secret_number:
            print("Lower!")
        else:
            print("Good job!")
            print(f"Number of attempts: {attempts}")
            break

    while True:
        play_again = input("Play again (y/n)? ").strip().lower()

        if play_again in ("y", "yes"):
            break
        elif play_again in ("n", "no", ""):
            exit()
        else:
            print("Please enter y or n.")

