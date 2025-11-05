n, q = map(int, input().split())


a = list(map(int, input().split()))

p = []
p.append(0)
for i in range(len(a)):
        soma = p[-1] + a[i]
        p.append(soma)

for i in range(q):
        a, b = map(int, input().split())
        print (p[b] - p[a-1])
