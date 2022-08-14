import random

N = int(input('Input number'))

matrix = [[random.randint(0, 500) for _ in range(N)] for _ in range(N)]
print(matrix)

# m = int(list(N[:] [N]))
# print(m)