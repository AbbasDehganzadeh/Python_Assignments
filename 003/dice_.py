import random

chance = 5
while chance:
    print("You have diced ", chance, " times")
    yes = input("Do you wanna dice?\t[y]es \t[n]o ")
    if yes[0] == "y":
        number = random.randint(1, 6)
        chance = chance - 1 if number != 6 else chance + 1
        print("your chance number is ", number)
    elif yes[0] == "n":
        print("روز خوبی داشته باشید.")
    else:
        continue

# end of rolling dice
print("مهلت شما به اتمام رسید")
