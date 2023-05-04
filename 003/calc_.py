import math

opt = input("Choose an option| \n\tA|a) basic \tB|b) advanced ")
operators = ["+", "-", "*", "x", "%"]
opt = "A" if opt is None else opt  # default option

if opt == "B" or opt == "b":  # In case its advanced
    operators.append(
        [
            "tan",  # tangent
            "cot",  # cotangent
            "sin",  # sinus
            "cos",  # cosinus
            "rad",  # radical
            "fac",  # factorial
        ]
    )

right = ""
# basic math mood
if opt == "A" or opt == "a":
    while right != "q":
        num_1 = int(input("Enter one number. "))
        num_2 = int(input("Enter another number. "))

        print("Enter an operator below")
        print(operators)
        oper = input()
        if oper == "+":
            print(num_1 + num_2)
        elif oper == "-":
            print(num_1 - num_2)
        elif oper == "*" or oper == "x":
            print(num_1 * num_2)
        elif oper == "%" and num_2 != 0:
            print(num_1 // num_2)
        else:
            print("Error: Invalid input,")
            break
        right = input("for quit press:(q|q)")
else:
    while right != "q":
        print("Enter an operator")
        print(operators)
        num_ = 1
        oper = input()
        if oper not in operators:
            print("Try again, maybe you should type correctly?")
            continue  # no need to continue

        num = int(input("Enter one number. "))
        radian = num * (math.pi / 360)
        if oper in ["+", "-", "*", "x", "%", "rad"]:
            num_ = int(input("Enter another number. ")) if num is not None else 2

        if oper == "rad":
            res = math.sqrt(num)
        elif oper == "fac":
            res = 1
            for i in range(num, 0, -1):
                res *= i
        elif oper == "cos":
            res = math.cos(radian)
        elif oper == "sin":
            res = math.sin(radian)
        elif oper == "tan":
            res = math.tan(radian)
        elif oper == "cot":
            res = 1 / math.tan(radian)
        elif oper == "+":
            res = num + num_
        elif oper == "-":
            res = num - num_
        elif oper == "*" or oper == "x":
            res = num * num_
        elif oper == "%" and num_ != 0:
            res = num // num_
        else:
            print("Error: Invalid input,")
            break
        print("result", res)
        right = input("for quit press:(q|q)")
