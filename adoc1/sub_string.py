n, q = map(int, input().split())

s = list(input())

cont = 0
for i in range (len(s)-2):
	if s[i] == "A" and s[i+1] == "B" and s[i+2] == "C":
		cont += 1 

for _ in range(q):
	x, c = input().split()
	i = int(x) - 1
	
	for j in range(i - 2, i + 1):
        	if 0 <= j <= len(s) - 3:
            		if s[j] == "A" and s[j+1] == "B" and s[j+2] == "C":
                		cont -= 1	
	
	s[i] = c
	
	for j in range(i - 2, i + 1):
        	if 0 <= j <= len(s) - 3:
            		if s[j] == "A" and s[j+1] == "B" and s[j+2] == "C":
                		cont +=1

		
	print (cont)
