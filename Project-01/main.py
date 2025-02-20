import random

numbers:list[int] = list(range(1, 11))
computer: int = random.choice(numbers)

print("\n🎮 Welcome to the Number Guessing Game! 🎮")
print("I have selected a number between 1 and 10. Can you guess it?")

user: int = int(input("\nEnter your guess: "))

if user == computer:
    print("\n🎉 Congratulations! You guessed the right number! 🎉")
else:
    print(f"\n❌ Wrong guess! The correct number was {computer}.")
    print("Better luck next time! Try again. 🔄")



