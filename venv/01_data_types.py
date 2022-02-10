print("We want your details!")

start = True

while start == True:
    try:
        name = str(input("What is your name?"))
        if name.isdigit() or name.isdecimal():
            print("Please enter a valid word")
        else:
            start = False

    except ValueError:
        print("Please enter a valid word")













start = True
while start == True:
    try:
        age = int(input("How old are you?"))
        print()
        start = False

    except ValueError:
        print("Please enter a valid number")



print(name)
print(age)
