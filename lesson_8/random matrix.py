import random

N = int(input('Input number'))

matrix = [[random.randint(0, 9) for _ in range(N)] for _ in range(N)]

print(matrix)

f = [list(i) for i in matrix() ]
print(f)
# for i in matrix:
#     x = i[i][-1]
# print(x)









