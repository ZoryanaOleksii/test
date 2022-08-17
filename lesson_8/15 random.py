import random

import random
el = 1
array = []
for el in range(15):
    array.append(random.randrange(1, 100, 1))
print(array)
odd = sum([i for i in array if i%2 == 0])
print('The sum of odd number is ' + str(odd))
even = sum([i for i in array if i%2 != 0])
print('The sum of  even number is ' + str(even))
#
if even > odd:
    print('True')
else:
    print('False')