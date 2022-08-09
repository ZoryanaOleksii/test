list_1 = list(input('input list with some indexes '))
k = int(input('Input k < len(list_1)'))
print('List original:' + str(list_1))

list_1[k:(k+1)] = []
print('List with shift left and delete [k]:' + str(list_1))

list_1.pop()
print('List with shift left and delete [k] and last index:' + str(list_1))
