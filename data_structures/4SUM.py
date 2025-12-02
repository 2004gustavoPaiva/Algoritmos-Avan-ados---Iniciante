n, x = map(int, input().split())
a = list(map(int, input().split()))

pares = []
for i in range(n):
    pares.append((a[i], i + 1))

pares.sort() 

for i in range(n):
    for j in range(i + 1, n):

        complemento = x - pares[i][0] - pares[j][0]

        l = j + 1
        r = n - 1

        while l < r:
            soma = pares[l][0] + pares[r][0]

            if soma == complemento:
                i1 = pares[i][1]
                i2 = pares[j][1]
                i3 = pares[l][1]
                i4 = pares[r][1]

                print(*sorted([i1, i2, i3, i4]))
                exit()

            if soma > complemento:
                r -= 1
            else:
                l += 1

print("IMPOSSIBLE")
