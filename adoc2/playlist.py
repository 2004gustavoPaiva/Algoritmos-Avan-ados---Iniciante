n = int(input())

a = list(map(int, input().split()))
l = 0
resp = 0
window = set()

for r  in range(n):
        nova = a[r] 

        while nova in window:

                antiga = a[l] 
                window.remove(antiga) 
                l += 1 


        window.add(nova) 


        resp = max(resp, r - l + 1)

print (resp)
