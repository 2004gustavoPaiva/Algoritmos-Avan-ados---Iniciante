t = int(input())

for _ in range (t):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    p = [0]
    soma = 0
    for i in range(len(a)):
        soma = p[-1] + a[i]
        p.append(soma)

    for _ in range (q):
        l, r, k= map(int, input().split())

        diferenca = r - (l-1)

        d = p[-1] - (p[r] - p[l-1])

        resultado = d + diferenca * k

        if resultado % 2 == 0:
            print ("NO")
        else:
            print ("YES")
