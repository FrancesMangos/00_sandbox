total_cost = 0.00
sugar_tax = 0.50

bread_type = input("Sandwich or Wrap?").lower()

filling_type = input("Meat, Vegetarian or Vegan?").lower()

pudding = input("Cookie, Chips, Fruit or None?").lower()

drink = input("Fizzy Drink, Water, Juice or None?").lower()

sauce = input("Would you like some extra sauce? Yes or No?").lower()

salad = input("Would you like an extra salad? Yes or No?").lower()

if bread_type != "sandwich":
    total_cost = 2.00
else:
    total_cost = 3.00

if filling_type == "vegetarian" or filling_type == "vegan":
    total_cost = total_cost + 1.00
else:
    total_cost = total_cost + 1.50

if pudding == "cookie" and drink == "fizzy drink":
    total_cost = total_cost + sugar_tax
if pudding == "cookie" or drink == "fizzy drink":
    total_cost = total_cost - 0.50
if sauce == "yes" and salad == "yes":
    total_cost = total_cost + 1.00

print("Your total cost is {}".format(total_cost))

