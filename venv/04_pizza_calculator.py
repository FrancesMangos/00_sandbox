total_cost = 0.00
voucher =  2.00

print("Welcome to Slice My Pizza 2: Electric Boogaloo!")
print("This time we won't slice your pizza though :D")

crust = input("Thick Crust or Thin Crust?").lower()

pizza_size = int(input("How large would you like your pizza to be? 8, 10, 12, 14, 18. Sizes are in inches"))

cheese = input("Do you want Cheese? Y/N").lower()

pizza_type = input("Which type of pizza would you like? Margarita, Vegetable, Vegan, Hawaiian, or Meat Feast?")

if crust != "thin crust":
    total_cost = 8.00
else:
    total_cost = 10.00

if pizza_size == 8 or pizza_size == 10:
    total_cost = total_cost + 0
else:
    total_cost = total_cost + 2.00

if cheese = ""

