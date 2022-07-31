# user put the year number
year = int(input('Please put year '))

# year should be between 1900 and 1000000
if year <=  1900 or year >= 1000000:
    print ('program end')

# if year divide by 400 it is leep
elif year % 400 == 0:
   print(str(year) + ' is leep year')

# if year divide by 100 it is not leep
elif year % 100 == 0:
   print(str(year + 'is not leep year'))

# if year divide by 4 it is leep
elif year%4 == 0:
   print(str(year) + ' is  leep year')

else:
   print(str(year) + ' is not leep year')
