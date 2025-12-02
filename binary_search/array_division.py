n, k = map(int, input().split())

a = list(map(int, input().split()))

l = max(a)
r = 10**22
res = 0
while l<=r:
	x = (r + l)//2
	soma = 0
	partition = 1
	for i in range(n):
		if (soma + a[i]) > x:
			soma = 0
			partition += 1
		soma += a[i]	

	if partition <= k:
		res = x
		r = x - 1
	else:
		l = x + 1

print (res)

