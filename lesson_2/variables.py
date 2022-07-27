# first variant
var1 = 50
var2 = 60
print (var1, var2)

var3 = var1
var1 = var2
var2 = var3
print(var1, var2)

# second variant
var1 = 50
var2 = 60
print(var1, var2)

var1, var2 = var2, var1
print(var1, var2)

# third variant
var1 = 50
var2 = 60
print (var1, var2)

var1 = var1 + var2
var2 = var1 - var2
var1 = var1 - var2
print(var1, var2)
