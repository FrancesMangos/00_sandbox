print("Welcome to Slice My Pizza!")
print()


while True:
    try:
        pizza_slices = int(input("How many slices are in your pizza?"))
    except ValueError:
            print("Please enter a valid number")
    continue

if pizza_slices > 0:
    while True:
        try:
            amount_people = int(input("How many people are sharing your pizza?"))
        except ValueError:
            print("Please enter a valid number")

if amount_people > 0:

    slices_each = pizza_slices//amount_people

    slices_remaining = pizza_slices%amount_people

print("Each person will get {} slices of pizza each".format(slices_each))
print()
print("There will be {} slices of pizza remaining".format(slices_remaining))
