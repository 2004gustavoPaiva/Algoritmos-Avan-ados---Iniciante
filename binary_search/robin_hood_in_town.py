t = int(input())

for _ in range(t):
	n = int(input())
	a = list(map(int, input().split()))
	if n < 3:
		print (-1)
	else:
		maxx = 0
		summ = 0
		for i in range(n):
			if (a[i] > a[maxx]):
				maxx = i
			summ += a[i]
		x = -1
		l = 0
		r = 10**15 
		poor = n // 2
		a.sort()
		while l <= r:
			mid  = (l + r)//2
			med = (summ+mid)/(2*n)
		
			if a[poor] < med:
				r = mid -1
				x = mid
			else:
				l = mid + 1
			
		print (x)
		
