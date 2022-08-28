import random

m = 4
matrix = [[random.randrange(1, 50) for _ in range(m)] for _ in range(m)]
# print(matrix)

print(matrix)
print(list(zip(*matrix)))
print(list(map(sum, zip(*matrix))))



matrix = matrix + [list(map(sum, zip(*matrix)))]



def foo():
    for i in range(m - 1):
        for j in range(m - i - 1):
            if matrix[j] > matrix[j + 1]:
                matrix[j], matrix[j + 1] = matrix[j + 1], matrix[j]
    return
print(matrix)



print('\n'.join('\t'.join(map(str, row)) for row in matrix))

