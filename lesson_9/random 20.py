import random
el = 1
array = []
for el in range(20):
    array.append(random.randrange(0, 21, 1))
print(array)

i = 0
keylist = [i for i in range(1, 21)]

print(keylist)

F = { key:value for (key, value) in zip(keylist, array)}
print(F)

