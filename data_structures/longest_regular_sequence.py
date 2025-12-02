s = input().strip()

sub_valida = [0] * len(s)
pilha = []

length = 0
cont = 0

for i in range(len(s)):
    c = s[i]

    if c == '(':
        pilha.append(i)
        continue

    if not pilha:
        continue

    j = pilha.pop()

    sub_valida[i] = i - j + 1
    if j - 1 >= 0:
        sub_valida[i] += sub_valida[j - 1]

    if sub_valida[i] > length:
        length = sub_valida[i]
        cont = 1
    elif sub_valida[i] == length:
        cont += 1

if length == 0:
    print(0, 1)
else:
    print(length, cont)
