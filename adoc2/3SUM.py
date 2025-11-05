n, x = map(int, input().split())

a = list(map(int, input().split()))

pares = []
for j in range(n):
	pares.append((a[j], j + 1))
pares.sort()
encontrado = False
for i in range(n):

	l = i + 1
	r = n -1	
	complemento = x - pares[i][0]
	
	while l < r:
		soma = pares[l][0] + pares[r][0]
		if soma == complemento:
			i1 = pares[i][1]
			i2 = pares[l][1]
			i3 = pares[r][1]
			encontrado = True
			print(*sorted([i1, i2, i3]))
			exit(0)
		if soma > complemento:
			r -= 1
		else:
			l += 1

if not encontrado:
	print ("IMPOSSIBLE")
