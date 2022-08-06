x = input('Put the sentence with 2 words')
n = ""
for i in x.split(" "): #return reverse words in sentence
    n = n + " " + i[::-1]

if  len(n.split()) != 2: # if input not 2 words
    print('need to put 2 words')
else:
    n = n.title()  # make title
    print(n)



