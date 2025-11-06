h, w = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(h)]

d = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(len(a)):
		
	for j in range(len(a[i])):
		if a[i][j] == 0:
			a[i][j] = "."
		else:
			a[i][j] = d[a[i][j]-1]
	
for l in range(len(a)):
	print("".join(a[l]))

