n, k = map(int, input().split())

a = sorted(list(map(int, input().split())))

l = 0
r = n - k -1
menor = a[r]- a[l]
while r < len(a):
	dif = a[r] - a[l]
	menor = min(menor, dif)
	l += 1
	r += 1

print (menor)
