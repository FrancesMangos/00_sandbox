total_cost = 0.00
voucher_money = 2.00

print("Welcome to Slice My Pizza 2: Electric Boogaloo!")
print("This time we won't slice your pizza though :D")
print()

crust = input("Thick Crust or Thin Crust?").lower()
print()

pizza_size= int(input("How large would you like your pizza to be? 8, 10, 12, 14, 18. Sizes are in inches"))
print()

cheese = input("Do you want Cheese? Y/N").lower()
print()

pizza_type = input("Which type of pizza would you like? Margarita, Vegetable, Vegan, Hawaiian, or Meat Feast?")
print()

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
