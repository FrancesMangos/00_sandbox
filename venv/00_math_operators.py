print("Welcome to Slice My Pizza!")
print()

pizza_slices = 0
amount_people = 0

while pizza_slices == 0:
    try:
        pizza_slices = int(input("How many slices are in your pizza?"))
        break
    except ValueError:
        print("Please enter a valid number")

while amount_people == 0:
    try:
        amount_people = int(input("How many people are sharing your pizza?"))
        break
    except ValueError:
        print("Please enter a valid number")


slices_each = pizza_slices//amount_people
print()
slices_remaining = pizza_slices%amount_people


print("Each person will get {} slices of pizza each".format(slices_each))
print()
print("There will be {} slices of pizza remaining".format(slices_remaining))
