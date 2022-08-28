x = list(input('Input some list with numbers'))
y = int(input('Input number'))

def param(x,y):

    i = 0
    j = 0
    for i in x:
        for j in x[i]:
            if x[j] + x[i] == y:
             print('true')
            else:
             print('no')

