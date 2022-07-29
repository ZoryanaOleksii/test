# put the number of pupils
K = int(input('How many pupils we have? '))

# put the number of apples
N = int(input(' How many apples we have? '))

# number of apples to 1 pupil
var = N // K
print('Every pupil have ' +str(var) + ' apples')

# number of apples left in box
var1 = N % K
print (str(var1) + ' aplles left in box')

print ('good bye')