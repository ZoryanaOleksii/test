txt = 'pythonlist'

y = 0

d = dict.fromkeys(txt, y)
print(d)

for i in d:
    d[i] = txt.count(i)
print(d)

