from random import randint
correct_number = randint(1, 10)

start = True
guesses_amount = 0
guess = ""

while start == True:
    try:
        guess = int(input("Guess a number between 1 and 10 (Don't repeat the same number!)"))
        print()
        guesses_amount += 1
        if guess == correct_number:
            print("Correct!")
            print("You got the number correct in {} attempts".format(guesses_amount))
            start = False
        elif guesses_amount == 3:
            print("You used up all three attempts")
            print("The correct number was {}".format(correct_number))
            start = False
        elif guess > correct_number:
            print("Incorrect!")
            print("The correct number is lower")
        elif guess < correct_number:
            print("Incorrect!")
            print("The correct number is between higher")
        else:
            print("Incorrect!")
    except:
        print("Please enter a number!")


