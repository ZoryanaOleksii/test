sum1 = 0
count = 0
count1 = 0
countall = 0

while True:
    n = int(input('Input numbers until zero  '))

    countall += 1 #all tryes

    if n == 0:
        break

    elif not n % 2:    #even
        count += 1
    elif n % 2: #odd
        count1 += 1

    sum1 += n
    av = sum1/countall


print('The number of even number = ' + str(count))
print('The number of odd number = ' + str(count1))
print('the sum of all elements is = ' + str(sum1))
print('the average sum except last = ' + str(av))
#print(str(max(n))
#print('the maximum is =  ' + str(ma))

   # print('the sum of all elements is = ' + str(sum(a)))
      #  print('the average sum except last = ' + str(av))
       # print('the minimum is = ' + str(min(s)))
        #print('the maximum is =  ' + str(max(s)))
        #print('the number of even number = ' + str(len(ev)))
        #print('the number of odd number = ' + str(len(od)))