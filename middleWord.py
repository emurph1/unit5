#Emily Murphy
#2017-11-13
#middleWord.py - prints out middle word

words = input('Enter words: ').split(' ')
if len(words)%2 == 0:
    print(words[len(words)//2-1:len(words)//2+1])
else:
    print(words[len(words)//2])

    
