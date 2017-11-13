#Emily Murphy
#2017-11-13
#middleWord.py - prints out middle word

words = input('Enter words: ').split(' ')
middleNum = len(words)
if middleNum%2 == 0:
    print(words[middleNum//2: middleNum-1])
else:
    print(words[middleNum//2)

    
