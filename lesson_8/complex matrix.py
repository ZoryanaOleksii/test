import random


N = int(input('Input number'))
matrix = [[i for i in range(-N, 0)] for j in range(0, N**2 - 1, N)]
print(matrix)