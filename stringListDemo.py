#Emily Murphy
#11/16/17
#stringListDemo.py	- prints	out	words	that	start	with	a	vowel
words = input('Enter some words: ').split('	')
for	word in	words:
	if	word[0]	in	'aeiouAEIOU':
		print(word)
