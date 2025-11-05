n = int(input())

prime = True
y = n - 2

for i in range(2,(y//2) +1):
        if y % i == 0:
                prime = False


if prime and y > 2:
        print (2, y)
else:
        print (-1)
