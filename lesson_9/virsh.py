x = " Любіть Україну, як сонце любіть, як вітер, і трави, і води... В годину щасливу і в радості мить, любіть у годину негоди.  Любіть Україну у сні й наяву, вишневу свою Україну, красу її, вічно живу і нову, і мову її солов"'"їну.   Без неї — ніщо ми, як порох і дим, розвіяний в полі вітрами... Любіть Україну всім серцем своїм і всіми своїми ділами.Для нас вона в світі єдина, одна, як очі її ніжно-карі... Вона у зірках, і у вербах вона, і в кожному серця ударі, у квітці, в пташині, в кривеньких тинах, у пісні у кожній, у думі, в дитячій усмішці, в дівочих очах і в стягів багряному шумі... '
x = x.replace(',', '')
x = x.replace('.', '')
# x = x.replace(' ', '')
x = x.replace('!', '')
x = x.replace('?', '')
x = x.replace('"', '')

x1 = x.split()
y = 0
d =  dict.fromkeys(x1, y)

for i in d:
    d[i] = x1.count(i)

print(d)

max_element = max(d.values())
print(max(d, key=d.get))
print(max_element)
# print("Max element of a dict: ", max_element, key=d.get)