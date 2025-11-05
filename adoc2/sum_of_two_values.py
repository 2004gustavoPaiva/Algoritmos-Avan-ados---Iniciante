import sys

n, x = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split())) 

if x <= 1:
        print("IMPOSSIBLE")
        exit(0)

m = {}
encontrado = False

for i in range(n):
    atual = a[i]
    alvo = x - atual
    
    if alvo in m:
        i1 = i + 1
        i2 = m[alvo] 
        print(min(i1, i2), max(i1, i2))
        encontrado = True
        break
    
    m[atual] = i + 1

if not encontrado:
    print("IMPOSSIBLE")
