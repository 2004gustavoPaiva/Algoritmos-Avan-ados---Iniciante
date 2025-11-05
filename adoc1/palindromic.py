l, r = map(int, input().split())

cont = 0
for i in range(l, r +1):
	s = str(i)
	if s == s[::-1]:
		cont += 1

print (cont)	
