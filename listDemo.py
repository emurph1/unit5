#Emily Murphy
#2017-11-13
#listDemo.py - print out first and last words in a list

words = input('Enter some words: ').split(' ') #everytime sees (space), it adds it to list

#print out lists one item per line
for w in words:
    print(w)

print('The first word was', words[0])
print('The last word was', words[-1]) #[-1] is always the last item in list