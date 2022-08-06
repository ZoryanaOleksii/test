n = int(input('Input number from 3 to 9'))

if n < 3 or n > 9:
    print('input the right number')
else:
      for i in range(n):
              for j in range(i+1):
                     print(j+1, end=" ")
              print("\n")