import random

print("🎮 Welcome to the Number Guessing Game!")

while True:
    secret_number = random.randint(1, 100)
    attempts = 0

    print("\nI have selected a number between 1 and 100.")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("📉 Too Low!")
        elif guess > secret_number:
            print("📈 Too High!")
        else:
            print("\n🎉 Congratulations! You guessed the correct number.")
            print("Total Attempts:", attempts)

            if attempts <= 5:
                print("🏆 Excellent!")
            else:
                print("👍 Good Job!")

            break

    choice = input("\nDo you want to play again? (Y/N): ").lower()

    if choice != "y":
        print("👋 Thanks for playing!")
        break