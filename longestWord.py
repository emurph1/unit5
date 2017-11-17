#Emily Murphy
#2017-11-15
#longestWord.py - find longest word in set of words

words = input('Enter words: ').split(' ')
lettercount = 0
maxletters = 0 
maxword = 0
for w in words:
    if len(w) > lettercount:
        lettercount = len(w)
    if lettercount > maxletters:
        maxletters = lettercount
        maxword = w
        lettercount = 0

print(maxword)

