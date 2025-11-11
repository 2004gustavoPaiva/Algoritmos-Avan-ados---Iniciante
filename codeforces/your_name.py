q = int(input())


for _ in range(q):
	n = int(input())
	t, s = map(str, input().split())
	cont = 0
	i = 0
	while i < n:
		for j in range(n):
			if t[j] == s[i]:
				cont += 1
				i+= 1
	if cont == n:
		print ("yes")
	else:
		print ("no")
