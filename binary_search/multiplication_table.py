n = int(input())

mid = n*n//2+1
l = 1
r = n*n
res = 0
while l<=r:
	soma = 0
	x = (r + l)//2
	for i in range(1, n+1):
		if (i<=x):
			soma += min(n, x//i)
	
	if soma >= mid:
		r = x - 1
		res = x
	else:
		l = x + 1

print (res)

