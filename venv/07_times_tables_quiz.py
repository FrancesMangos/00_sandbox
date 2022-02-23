
answer = 0

print("Welcome to the Times Table Quiz")

times_tables = int(input("Which times table would you like to see?"))
print()
highest_value = int(input("What is the highest value you would like to go to?"))
highest_value = highest_value + 1
print()

print("You will be tested the {} times tables".format(times_tables))
print()
for x in range(1, highest_value):
    answer = x * times_tables
    user_guess = int(input("What is {} times {}?".format(x, times_tables)))
    if user_guess == answer:
        print("Correct!")
        print("{} times {} is {}".format(x, times_tables, answer))
        print()
    else:
        print("Incorrect!")
        print("{} times {} is {}".format(x, times_tables, answer))
        print("Your answer was {}".format(user_guess))
        print()
