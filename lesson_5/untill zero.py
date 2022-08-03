s = set()
while (x := int(input("Enter number: "))) != 0:
    s.add(x)

#average
av = sum(s)/len(s)

#even
ev = [int(i) for i in s if i % 2 == 0]

#odd
od = [int(i) for i in s if i % 2 != 0]





print('the sum of all elements is = ' + str(sum(s)))
print('the average sum except last = ' + str(av))
print('the minimum is = ' + str(min(s)))
print('the maximum is =  ' + str(max(s)))
print('the number of even number = ' +  str(len(ev)))
print('the number of odd number = ' +  str(len(od)))

