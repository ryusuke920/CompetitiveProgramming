import math
n = int(input())
a = list(map(int,input().split()))
a.sort(reverse = True)
ans = 0
for i in range(n):
    if i == 0: continue
    if i == 1:
        ans += a[0]
    else:
        ans += a[math.floor(i/2)]
print(ans)