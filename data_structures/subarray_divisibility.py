entrada = input().split()
n = int(entrada[0])

a = list(map(int, input().split()))

d = {}
d[0] = 1

s = 0
res = 0

for x in a:
    s += x
    r = s % n
    if r < 0:
        r += n
    if r in d:
        res += d[r]
        d[r] += 1
    else:
        d[r] = 1

print(res)
