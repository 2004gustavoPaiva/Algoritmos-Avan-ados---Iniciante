n = int(input())

res = 0
for _ in range(n):
	a = list(map(int, input().split()))
	cont = 0
	for j in range(3):
		if a[j] == 0:
			cont += 1
	if cont <= 1:
		res +=1
	
print (res)
