n = int(input())

array = [n]

while n != 1:
	if n % 2 == 0:
		n = n //2
		array.append(n)
	else:
		n = n * 3 + 1
		array.append(n)



print (*array)


