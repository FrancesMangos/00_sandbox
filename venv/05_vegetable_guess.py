print("Welcome to Vegetable Guess!")
print()
print("Choose a vegetable as your choice and we will try and guess it!")
print("Choose between: Carrot, Peas, Broccoli, Sweetcorn")
print()

guess_one = input("Is your vegetable green? Y/N").lower()
if guess_one == "y" or guess_one == "yes":
    guess_two = input("Is your vegetable shaped like a tree?").lower()
    if guess_two == "y" or guess_two == "yes":
        print("It must be a Broccoli!")
    else:
        print("It must be Peas!")

else:
    guess_three = input("Is your vegetable yellow?").lower()
    if guess_three == "y" or guess_three == "yes":
        print("It must be a Sweetcorn!")
    else:
        print("It must be a Carrot!")
