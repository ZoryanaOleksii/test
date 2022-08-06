stg = input('enter 2 words')
stg = stg + ' '
temp = ""
rev = ""
for i in stg:
    if i != ' ':
        temp = i + temp
    else:
        rev = rev + " " + temp
        temp = ""
    print(rev)