s = input()

conjunto = set()

for letter in s:
	conjunto.add(letter)

if len(conjunto) % 2 == 0:
	print ("CHAT WITH HER!")
else:
	print ("IGNORE HIM!")


