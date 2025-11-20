n, t = map(int, input().split())

a = list(map(int, input().split()))

r = 10**18
l = 1
res = 0
while l <= r:
	mid = (r + l) // 2
	cont = 0
	for j in range(n):
		if a[j] <= mid:
			cont += mid//a[j]
	if cont >= t:
		res = mid
		r = mid - 1
	else:
		l = mid + 1


print (res)
