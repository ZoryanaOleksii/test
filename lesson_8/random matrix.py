import random


N = input('Input number')
matrix = [[random.randint(0, 10) for _ in range(N)] for _ in range(N)]

print(matrix)

g = sum(matrix[i][-1] for i in matrix)








