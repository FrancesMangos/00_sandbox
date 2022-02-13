print("We want your details!")


start = True
while start == True:
    try:
        name = str(input("What is your name?"))
        print()
        if name.isdigit() or name.isdecimal():
            print("Please enter a valid word")
        else:
            start = False

    except ValueError:
        print("Please enter a valid word")
name = name.title()
name = name.strip()


start = True
while start == True:
    try:
        age = int(input("How old are you?"))
        print()
        start = False

    except ValueError:
        print("Please enter a valid number")

start = True
while start == True:
    try:
        fave_icecream = str(input("What is your favourite icecream flavour?"))
        print()
        if fave_icecream.isdigit() or fave_icecream.isdecimal():
            print("Please enter a valid icecream flavour")
        else:
            start = False

    except ValueError:
        print("Please enter a valid icecream flavour")
fave_icecream = fave_icecream.title()

start = True
while start == True:
    try:
        fave_animal = str(input("What is your favourite animal?"))
        print()
        if fave_animal.isdigit() or fave_animal.isdecimal():
            print("Please enter a valid animal")
        else:
            start = False
    except ValueError:
        print("Please enter a valid animal")
fave_animal = fave_animal.title()

start = True
while start == True:
    try:
        pi_guess = float(input("Try and name the first three decimals of Pi."))
        print()
        start = False
    except ValueError:
        print("Please enter valid numbers")




print("Your name is {}".format(name))
print("You are {} years old.".format(age))
print("Your favourite icecream flavour is {} Icecream!".format(fave_icecream))
print("Your favourite animal is a {}!".format(fave_animal))
if pi_guess == 3.141:
    print("You said Pi to be 3.141 and you got it correct!")
else:
    print("You said Pi to be {} but Pi is actually 3.141, meaning you sadly got it incorrect.".format(pi_guess))



