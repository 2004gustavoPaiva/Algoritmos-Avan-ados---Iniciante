import sys

sys.stdin = open("bcount.in", "r")
sys.stdout = open("bcount.out", "w")

n, q = map(int, input().split())

vacas = [[0, 0, 0]]
soma1 = soma2 = soma3 = 0

for i in range(1, n + 1):
    vaca = int(input())
    if vaca == 1:
        soma1 += 1
    elif vaca == 2:
        soma2 += 1
    else:
        soma3 += 1
    vacas.append([soma1, soma2, soma3])

for _ in range(q):
    l, r = map(int, input().split())
    print(
        vacas[r][0] - vacas[l - 1][0],
        vacas[r][1] - vacas[l - 1][1],
        vacas[r][2] - vacas[l - 1][2]
    )
