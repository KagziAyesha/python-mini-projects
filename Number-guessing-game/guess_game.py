import random 

print("Welcome to number-guessing game!")

print("Choose Difficulty Level:")
print("1.Easy (1-50,  10 Attempts)")
print("2.Medium (1-100,  7 Attempts)")
print("3.Hard (1-200,  5 Attempts)")

choice=input("Enter Your Choice(1/2/3):")

if choice == "1":
    max_number=50
    max_attempt=10
elif choice == "2":
    max_number=100
    max_attempt=7
else:
    max_number=200
    max_attempt=5

number=random.randint(1, max_attempt)
attempts=0

while attempts < max_attempt:
    try:
        guess=int(input(f"Guess the number (1 to {max_number}):"))
    except ValueError:
        print("❌Please enter a valid number")
        continue

    attempts+=1

    if guess < number:
        print("Too low! Try again")
    elif guess > number:
        print("Too high! Try again")
    else:
        print("Congratulations🎉")
        print("You guessed the number in",attempts,"attempts")
        break
else:
    print("Game over😕!")
    print("The correct number was",number)

print("Thank You for playing☺️")