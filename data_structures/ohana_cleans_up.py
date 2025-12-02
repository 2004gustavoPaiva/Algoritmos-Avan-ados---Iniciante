n = int(input())

linhas = []

for _ in range(n):
	linhas.append(input().strip())

d = {}
for linha in linhas: 
	if linha in d:
		d[linha] += 1
	else:
		d[linha] = 1
	

print (max(d.values()))


