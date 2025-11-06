n = int(input())

a = list(map(int, input().split()))

aux = []

for i in range(n):
	if a[i] % 2 == 0:
		aux.append(a[i])

print (*aux)
