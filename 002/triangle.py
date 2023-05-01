# a programme for showing that is triangle or not

a = int(input())
b = int(input())
c = int(input())

if a >= b + c or \
    b >= a + c or \
    c >= a + b:
    print("not trangular")
else:
    print("trangular")
