n ,k = map(int, input().split())

a = list(map(int, input().split()))
a.sort()
m = n//2
res = 0
l = 1
r = 2 * 10**9
while l <= r:
	soma = 0
	x = (r + l)//2
	for i in range(m, n):
		if (x - a[i]) >= 0:
			soma += (x - a[i])
	if soma <= k:
		l = x + 1
		res = x
	else:
		r = x - 1

print (res) 

