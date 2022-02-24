not_validated = True

while not_validated == True:
    try:
        number = int(input("Enter a number between 1 and 10"))
        if number > 1 and number < 11:
            not_validated = False
        else:
            print("Number entered out of range")
    except ValueError:
        print("You must enter a number between 1 and 10")
