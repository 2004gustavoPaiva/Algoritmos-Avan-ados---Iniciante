import sys

data = sys.stdin.read().split()
ptr = 0

n = int(data[ptr]); ptr += 1
x = int(data[ptr]); ptr += 1

a = list(map(int, data[ptr:ptr+n]))
ptr += n

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

