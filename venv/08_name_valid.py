name = ""

while name == "":
    try:
        name = input("Enter a name:")
        if name == "":
            print("Name cannot be left blank")
    except ValueError:
        print("Please enter a valid word, name cannot be blank")

print("Stored name: {}".format(name))
