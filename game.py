import random

print("================================")
print("     NUMBER GUESSING GAME")
print("================================")

secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 7

print("\nI have selected a number between 1 and 100.")
print(f"You have {max_attempts} attempts to guess it.")

while attempts < max_attempts:

    try:
        guess = int(input("\nEnter your guess: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if guess < 1 or guess > 100:
        print("Please enter a number between 1 and 100.")
        continue

    attempts += 1

    if guess < secret_number:
        print("Too low! 📉")

    elif guess > secret_number:
        print("Too high! 📈")

    else:
        print("\n🎉 Congratulations!")
        print(f"You guessed the number in {attempts} attempts.")
        break

else:
    print("\n❌ Game Over!")
    print(f"The correct number was {secret_number}.")