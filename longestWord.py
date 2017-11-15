#Emily Murphy
#2017-11-15
#longestWord.py - find longest word in set of words

words = input('Enter words: ').split(' ')
longest = 0
word = ' '
for w in words:
    if len(w) > longest:
        longest = len(w)
        for w in words:
            longest = len(w)
        print(w)

