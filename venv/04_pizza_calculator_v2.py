total_cost = 0.00
voucher_money = 2.00

print("Welcome to Slice My Pizza 2: Electric Boogaloo!")
print("This time we won't slice your pizza though :D")
print()

start = True
while start == True:
    try:
        crust = input(str("Thick Crust or Thin Crust?")).lower()
        print()
        if crust == "thick" or crust == "thin":
            start = False
        else:
            print("Please enter a valid crust thickness")

    except ValueError:
        print("Please enter either thin or thick")

start = True
while start == True:
    try:
        pizza_size= int(input("How large would you like your pizza to be? 8, 10, 12, 14, 18. Sizes are in inches"))
        print()
        if pizza_size == 8 or pizza_size == 10 or pizza_size == 12 or pizza_size == 14 or pizza_size == 18:
            start = False
        else:
            print("Not a valid pizza size")
    except ValueError:
        print("Please enter a pizza size")

start = True
while start == True:
    try:
        cheese = input(str("Do you want Cheese? Y/N")).lower()
        print()
        if cheese == "yes" or cheese == "y" or cheese == "no" or cheese == "n":
            start = False
        else:
            print("Please enter yes or no")

    except ValueError:
        print("Please enter yes or no")

start = True
while start == True:
    try:
        pizza_type = input(str("Which type of pizza would you like? Margarita, Vegetable, Vegan, Hawaiian, or Meat Feast?")).lower()
        print()
        if pizza_type.isdigit() or pizza_type.isdecimal():
            print("Please enter a valid pizza type")
        else:
            if pizza_type == "margarita" or pizza_type == "vegetable" or pizza_type == "vegan" or pizza_type == "hawaiian" or pizza_type == "meat feast":
                start = False
            else:
                print("Not valid pizza type")

    except ValueError:
        print("Please enter a valid pizza type")

if crust != "thin crust":
    total_cost = 8.00
else:
    total_cost = 10.00

if pizza_size != 8 or pizza_size != 10:
    total_cost = total_cost + 2.00
else:
    total_cost = total_cost + 0.00

if cheese == "y" or cheese == "yes":
    total_cost = total_cost - 0.50
else:
    total_cost = total_cost + 0.00

if pizza_type == "margarita":
    total_cost = total_cost + 0.00
elif pizza_type == "vegetable" or pizza_type == "vegan":
    total_cost = total_cost + 1.00
else:
    total_cost = total_cost + 2.00

if pizza_size == 18:
    voucher = input("Do you have a voucher? Y/N").lower()
    if voucher == "y" or voucher == "yes":
        voucher_name = input("What is the name of your voucher? For confirmation.").lower()
        if voucher_name == "funfriday":
            print("Ahh, since you have the voucher code FunFriday, you get $2 off your pizza purchase.")
            total_cost = total_cost - voucher_money
            print()

        else:
            print("Unfortunately that voucher code is incorrect.")
            print()

    else:
        print("It seems you do not have a voucher.")
        print()

print("Your {} crust {} inch {} pizza will cost a total of {:.2f}".format(crust, pizza_size, pizza_type, total_cost))
