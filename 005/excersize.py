# An excessive programme,


def solve_square(a, b, c):
    delta = b**2 - 4 * a * c
    if delta >= 0:
        a1 = (-b + delta**0.5) / (2 * a)
        a2 = (-b - delta**0.5) / (2 * a)
        return {a1, a2}
    return "ArgumentError"


def fibbo(num):
    if num == 1 or num == 2:
        return 1
    return fibbo(num - 1) + fibbo(num - 2)


w, h = input().split()
W, H = int(w), int(h)
for i in range(W):
    for j in range(H // 2):
        if i % 2 == 0:
            print("#*", end="")
        else:
            print("*#", end="")
    print()

ans = solve_square(4, 2, 0)
print("The solution:", ans)

fibs = []
for i in range(int(input("Fibonacci questions\t"))):
    fibs.append(fibbo(i + 1))
print("Fibonacci answers", *fibs)
