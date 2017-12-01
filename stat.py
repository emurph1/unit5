#Emily Murphy
#2017-12-01
#stat.py - 

numbers = []

while True:
    nums = input('Enter q to quit. Enter numbers: ')
    if nums == 'q':
        break
    numbers.append(nums)
numbers.sort()
print('Max is ', numbers[len(numbers)-1])
print('Min is ', numbers[0])

total = 0
for i in numbers:
    total += float(i)
    mean = total/len(numbers)
print('Mean is ', mean)

for j in numbers:
    