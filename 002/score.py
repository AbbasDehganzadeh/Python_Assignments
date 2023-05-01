score_1 = float(input())
score_2 = float(input())
score_3 = float(input())

# Logical terms
avg_ = (score_1 + score_1 + score_1) / 3
if avg_ > 17:
    print("Graet")
elif avg_ >= 10:
    print('normal')
else:
    print("Failed")
