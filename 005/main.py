# matrices = list() # Initialization variable

# for i in range(10):
# 	matrices.append([i+1])
# 	for j in range(2, 11):
# 		matrices[i].append((i+1)*j)

# for x in matrices:
# 	for y in x:
# 		if y >= 10:
# 			print(y, end=' ')
# 		else:
# 			print('', y, end=' ')
# 		# print(y, end=' ')
# 	print()






############################@@@@
def expo(a, b):
	return a**b

result = []
for i in range(100):
	result.append(expo(2, i+1))
print(result)
