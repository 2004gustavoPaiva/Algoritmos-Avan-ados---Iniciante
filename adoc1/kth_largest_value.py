n, q = map(int, input().split())

array =  list(map(int, input().split()))

cont = 0
for i in range (len(array)):
	if array[i] == 1:
		cont += 1
for j in range(q):
	t, x = map(int, input().split())
	if t == 1:
		if array[x-1] == 1:
			cont -= 1
		
		else:
			cont += 1
		array[x-1] = 1- array[x-1]
	else:
		if x <= cont:
			print(1)
		else:
			print(0)

	

	
		
