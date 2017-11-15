#Emily Murphy
#2017-11-15
#dictionaryDemo.py 

dictionary = ['alphabet', 'sweatshirt', 'sweatpants', 'shorts', 'computer', 'waterbottle']

dictionary.sort()

number = int(input('What number word do you want to look up? '))
if number >= len(dictionary):
    print('Invalid')
else:  
    print('Word number', number, 'is', dictionary[number-1])