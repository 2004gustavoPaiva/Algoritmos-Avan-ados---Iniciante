import sys
n = int(input())

a = list(map(int, input().split()))

l = 0
r = len(a) -1
sum1 = a[l]
sum3 = a[r]
resposta = 0
while l < r:
	if sum1 < sum3:
		sum1 += a[l+1]
		l += 1
	elif sum1 > sum3:
		sum3 += a[r-1]
		r -= 1
	else:	
		resposta = sum1
		sum1 += a[l+1]
		l += 1

print (resposta)
