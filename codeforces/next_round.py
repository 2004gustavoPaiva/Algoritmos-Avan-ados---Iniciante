n, k = map(int, input().split())

a = list(map(int, input().split()))

if a[0] == 0:
	print (0)
	exit(0) 
qtd = 0
for i in range(len(a)):
	if a[i] >= a[k-1] and a[i] > 0:
		qtd += 1


print (qtd)
