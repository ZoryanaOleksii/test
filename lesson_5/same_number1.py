N = list(str(input('Input number')))
k = int(len(N))

for i in range(k-1):
    for j in range(i+1, k):
        if N[i] == N[j]:
            print("Have same elements")
            quit()
print("All elements unique")



