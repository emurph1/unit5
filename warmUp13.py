#Emily Murphy
#11/16/17
#warmup13.py	- make	a	list	of	20	random	numbers,	print	out	sum,	min,	and	max
from	random	import	randint
numbers	=	[]
for	i	in	range(20):
				numbers.append(randint(1,100))
print('The	min	is',	min(numbers))
print('The	max	is', max(numbers))
print('The	sum	is',	sum(numbers))
