import random


N = input('Input number')
matrix = [[random.randint(0, 10) for _ in range(N)] for _ in range(N)]

print(matrix)

g = sum((i[-1] for i  in matrix ))
print(g)








