n = int(input())

a = list(map(int, input().split()))

pilha = []

res = [0] * n

for i in range(n):
	while pilha and pilha[-1][0] >= a[i]:
		pilha.pop()
	

	if pilha:
		res[i] = pilha[-1][1]
	else:
		res[i] = 0

	pilha.append((a[i], i+1))
	

print (*res)

