import math

t = int(input())

for _ in range(t):
	k = int(input())
	l = 0
	r = 4 * 10**18
	res = r
	while l <= r:
		n = (r + l) //2
		key = n - math.isqrt(n)
		if key >= k:
			res = n
			r = n - 1
		else:
			l = n + 1
		
	print (res)

		
