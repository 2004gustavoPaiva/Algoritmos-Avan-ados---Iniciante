n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a1 = []
b1 = []
i = 0
j = 0
pos = 1
while (i< n and j< m):

	if(a[i] <= b[j]):
		a1.append(pos)
		i += 1
	else:
		b1.append(pos)
		j+=1
	pos += 1
	
while (i<n):
	a1.append(pos)
	i+= 1
	pos += 1

while (j<m):
	b1.append(pos)
	j+=1
	pos += 1


print (*a1)
print (*b1)
