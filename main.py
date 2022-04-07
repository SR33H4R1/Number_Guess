import random

# Number guessing game by SREEHARI

r1, r2 = input("Enter the range (eg: 5 20) : ").split()  # Getting range from user

comp = random.randint(int(r1), int(r2))  # Computer choosing a random number

user = None

while comp != user:
    user = int(input("\nEnter your guess : "))  # User guessing a number

    if user > int(r2):     # Checking if user input in the given range
        print("\nYour choice was larger than the limit. Please choose a number inside the limit.")
        continue
    elif user < int(r1):
        print("\nYour choice was smaller than the limit. Please choose a number inside the limit.")
        continue
    else:

        if user == comp:
            print("Congrats you guessed correct !!!")
        elif user < comp:
            print("Try again. You guessed too small.")
        else:
            print("Try again. You guessed too large.")
