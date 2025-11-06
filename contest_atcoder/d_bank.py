n, q = map(int, input().split())

a = list(range(n, 0, -1))
c = []
for i in range(q):
	query = input().split()
	
	if query[0] == "2":
		if query[1] == a[len(a) - 1]:
			a.pop()
	elif query[0] == "3":
		c.append(a[len(a)-1])
		

for j in range(len(c)):
	print (c[j])
	
