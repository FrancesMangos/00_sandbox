print("Welcome to Slice My Pizza!")
print()

try:
    pizza_slices = (int(input("How many slices are on your pizza?")))
    print()

try:
    amount_people = (int(input("How many people are sharing this pizza?")))
    print()

slices_each = pizza_slices/amount_people

slices_remaining = pizza_slices%amount_people

print("Each person will get {} slices of pizza each".format(slices_each))
print()
print("There will be {} slices of pizza remaining".format(slices_remaining))
