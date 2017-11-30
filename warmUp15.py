#Emily Murphy
#2017-11-30
#warmUp15.py - function that take a list of numbers as argument and returns the list where each number is doubled

def doubled(n):
    new = []
    for i in n:
       new.append(i*2)
    return new
    
print(doubled([2,4,6]))