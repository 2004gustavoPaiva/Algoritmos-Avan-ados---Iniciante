t = int(input())

for _ in range(t):

	n = int(input())
	pessoas = list(map(int, input().split()))
	tempo = list(map(int, input().split()))
	
	res = 0
	l = 0
	r = 10**10
	for _ in range(100):
		T = (r+l)/2.0
		max_esquerda = -100000000000000
		min_direita = 100000000000000
		possivel = True
		for i in range(n):
			if (T-tempo[i]) < 0:
				possivel = False
				break
		
			esquerda = pessoas[i] - (T - tempo[i])
			direita = pessoas[i] + (T - tempo[i])
			if esquerda > max_esquerda:
				max_esquerda = esquerda
			if direita < min_direita:
				min_direita = direita
		
		if possivel and  min_direita >= max_esquerda:
			r = T - 1
			res = max_esquerda
		else:
			l = T + 1

	print(f"{res:.7f}")

