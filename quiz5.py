#Emily Murphy  
#2017-12-04
#quiz5.py

from random import randint
def rand5():
    nums= []
    for i in range (1,6):
        nums.append(randint(1,100))
    return nums

def lastElement(element):
    elements = []
    elements.append(element)
    return element[-1]

def wordLengths(words):
    word = []
    for w in words:
        word.append(len(w))
    return word

print(lastElement(['cat','dog','rat']))
print(rand5())
print(wordLengths(['the', 'cat', 'is', 'hungry']))