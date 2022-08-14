import random

import random
el = 1
array = []
for el in range(15):
    array.append(random.randrange(0, 15, 1))
print(array)
odd = len([i + 1 for i in array if i%2 == 0])
print('Number of odd number is ' + str(odd))
even = len([i + 1 for i in array if i%2 != 0])
print('Number of even number is ' + str(even))

if even > odd:
    print('True')
else:
    print('False')