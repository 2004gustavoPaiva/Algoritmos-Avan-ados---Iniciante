m = []
for _ in range(5):
	a = list(map(int, input().split()))
	m.append(a)

index = (0, 0)
for i in range(len(m)):
	for j in range(len(m[i])):
		if m[i][j] == 1:
			index = (i, j)

res = abs(index[0] - 2) + abs(index[1] - 2)

print (res) 
