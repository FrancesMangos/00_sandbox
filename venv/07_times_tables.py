
answer = 0

times_tables = int(input("Which times table would you like to see?"))
print()

print("Here is the {} times tables".format(times_tables))
for x in range(1, 13):
    answer = x * times_tables
    print("{} times {} is {}".format(x, times_tables, answer))
