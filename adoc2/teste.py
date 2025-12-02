import sys

input = sys.stdin.readline

n, x = map(int, input().split())

a = list(map(int, input().split()))
if x == 1:
	print (0)
	exit(0)
cont = 0

d = {0: 1}

soma = 0
for j in range(n):
	soma += a[j]
	complemento = soma - x

	if complemento in d:
		cont += d[complemento]


	d[soma] = d.get(soma, 0) + 1

print (cont)
