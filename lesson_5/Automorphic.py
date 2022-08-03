N = int(input('input number  '))

print('The automorphic numbers are:, ', end=' ')
#finding an automorphic numbers
for i in range (0, N+1):
    sq = i*i
    tmp = i

    while i>0:
        if (sq%10)!=(i%10):
            break
        sq//=10
        i//=10
    if i == 0:
        print(tmp, end=' ')
    i = tmp