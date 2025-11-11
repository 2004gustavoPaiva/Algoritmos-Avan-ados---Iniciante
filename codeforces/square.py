n = int(input())

for j in range(n):
	square = True
	a = list(map(int, input().split()))
	element = a[0]
	for i in range(len(a)):
		if (a[i] != element):
			square = False
	if square:
		print ("yes")
	else:
		print ("no")
