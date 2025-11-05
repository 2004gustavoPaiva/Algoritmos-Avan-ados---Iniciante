a = list(map(int, input().split()))

while len(a) != 64:
	a = list(map(int, input().split()))

resultado = 0
for i in range (len(a)):
	if a[i] != 0:
		resultado +=  2**i

	
print (resultado)
