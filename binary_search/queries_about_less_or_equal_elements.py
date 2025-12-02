n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
res = []
for j in range(m):
	i = -1
	l = 0
	r = n -1
	while l<=r:
		mid = (r + l)//2
		if (a[mid] <= b[j]):
			l = mid + 1
			i = mid
		else:
			r = mid - 1
	res.append(i +1)
		
print (*res)
