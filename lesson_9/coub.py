key_1 = [i for i in range(1, 11)]
print(key_1)

value_1 = [i**3 for i in range(1, 11)]
print(value_1)

F = { key:value for (key, value) in zip(key_1, value_1)}
print(F)