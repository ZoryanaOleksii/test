
n = int(input("Input number "))

i = 1
while i ** 2 <= n:
    print(i ** 2, end=' ')
    i += 1

print('\n Last number', i - 1)
