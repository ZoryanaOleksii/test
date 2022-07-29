# number of pupils in first class
class1 = int(input('How many pupils we have in first class? '))

# number of pupils in second class
class2 = int(input('How many pupils we have in second class? '))

#number of pupils in third class
class3 = int(input('How many pupils we have in third class? '))

#numbers of tables for first class

x1 = class1//2

if x1%2 != 0:
    x1 = x1 + 1
else: x1 = x1

#numbers of tables for second class
x2 = class2//2

if x2%2 != 0:
    x2 = x2 + 1
else: x2 = x2

x3 = class3//2

#numbers of tables for third class
x3 = class3//2
if x3%2 != 0:
    x3 = x3 + 1
else: x3 = x3

xsumm = x1 + x2 + x3

print('We need ' + str(xsumm) + ' tables')




