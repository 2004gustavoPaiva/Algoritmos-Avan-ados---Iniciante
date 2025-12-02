import sys

#tive que usar essa maneira estranha de receber dados ja que aqui (em Python) tava dando TLE, fui verificar a solucao no codeforces em c++ e ela fazia a exata mesma coisa.

entrada = sys.stdin.read().split()

if not entrada:
    print(0)
    sys.exit()

n = int(entrada[0])

l = []
i = 1

for _ in range(n):
	if i + 1 >= len(entrada):
		break
	a = int(entrada[i])
	b = int(entrada[i+1])
	i += 2


	
	t = (a, 1)
	t2 = (b, -1)
	l.append(t)
	l.append(t2)

l.sort()
soma  = 0
maior = 0
for i in range(len(l)):
	soma += l[i][1]
	if soma > maior:
		maior = soma

print (maior)

