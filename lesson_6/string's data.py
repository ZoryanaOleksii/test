n = input('input string with more than 15 characters')

print(n[2])  # print [3] character
print(n[-2])  # print before last
print(n[:5])  # the first 5
print(n[:-2])  # except last 2
print(n[::2])  # all even
print(n[1::2])  # all od
print(n[::-1])   # reverse string
k = n[::-1]
print(k[::2])   # reverse + even
print(len(n))

