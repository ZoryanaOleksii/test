var1 = list(input('Input the first list'))
var2 = list(input('Input the second list'))

var3 = var1 + var2


output = []
for x in var3:
    if x not in output:
        output.append(x)
print(len(output))

