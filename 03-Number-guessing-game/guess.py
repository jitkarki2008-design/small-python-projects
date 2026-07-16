# Project 03 - Number Guessing Game
import random

print("--- Number Guessing Game ---")
print("I'm thinking of a number between 1 and 100")

secret_number = random.randint(1, 100)
attempts = 0

while True:
    try:
        guess = int(input("\nEnter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try bigger ^")
        elif guess > secret_number:
            print("Too high! Try smaller v")
        else:
            print(f"\n🎉 Correct! The number was {secret_number}")
            print(f"You guessed it in {attempts} attempts")

            if attempts <= 3:
                print("Rank: Pro Gamer 🔥")
            elif attempts <= 6:
                print("Rank: Smart Player 👏")
            else:
                print("Rank: Keep Practicing 💪")
            break

    except ValueError:
        print("Please enter a number only!")