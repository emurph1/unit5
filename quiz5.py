#Emily Murphy  
#2017-12-04
#quiz5.py

from random import randint

def rand5(num):
    nums = []
    for i in range(num):
        nums.append(i)
        if len(nums) == 5:
            break
    return nums

print(rand5(randint(1,100)))

