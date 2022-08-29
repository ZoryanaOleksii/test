import random


N = int(input('Input number'))

matrix = [[random.randint(0, 10) for _ in range(N)] for _ in range(N)]

print(matrix)

g = sum((i[-1] for i  in matrix ))

print( 'Sum of last column = '+ str(g))
i = 1
s = sum(matrix[i][i] for i in range(N))
print('Sum of diagonal = ' + str(s))








