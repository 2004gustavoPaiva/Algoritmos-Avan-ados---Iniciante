n = int(input())

for i in range (n):
	s = input()
	if len(s) <= 10:
		print (s)
	else:
		aux = ''
		cont = 0
		for j in range(1, len(s)-1):
			cont += 1
		aux = s[0] + str(cont) + s[len(s) -1]
		print (aux)
			
