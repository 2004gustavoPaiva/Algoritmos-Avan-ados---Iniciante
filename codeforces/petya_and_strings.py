
s1 = input().lower()
s2 = input().lower()

diferenca = False
for i in range (len(s1)):
	if s1[i] > s2[i]:
		print (1)
		diferenca = True
		break
	elif s1[i] < s2[i]:
		print (-1)
		diferenca = True
		break
	
if not diferenca:
	print (0)
	
