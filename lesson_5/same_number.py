number = list(input('put number'))


if len(number) == len(set(number)):
    print('no')
else:
    print('yes')