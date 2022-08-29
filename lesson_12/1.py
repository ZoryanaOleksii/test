import random

m = 4
matrix = [[random.randrange(1, 50) for _ in range(m)] for _ in range(m)]
# print(matrix)

# print(matrix)
# print(list(zip(*matrix)))
# print(list(map(sum, zip(*matrix))))



# matrix = matrix + [list(map(sum, zip(*matrix)))]
i = 0
j = 0
for i in range(m):
    for j in range(m):
        if matrix[i][j] > matrix[i+1][j]:
            matrix[i][j], matrix[i + 1][j] = matrix[i + 1][j], matrix[i][j]
print(matrix)



# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         if matrix[i][j] > matrix[i][j + 1]:
#             matrix[j], matrix[j + 1] = matrix[j + 1], matrix[j]
#         print(matrix)



# print('\n'.join('\t'.join(map(str, row)) for row in matrix))

