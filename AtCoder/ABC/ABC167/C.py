n, m, x = map(int, input().split())
a = []
b = []
for i in range(n):
    ca = list(map(int,input().split()))
    a.append(ca[0])
    b.append(ca[1:])

ans = 10**9
for i in range(1 << n):
    money = 0
    ex = [0]*m
    for j in range(n):
        if (i >> j) & 1 == 0: continue
        money += a[j]
        for k in range(m):
            ex[k] += b[j][k]
    if all(x <= l for l in ex):
        ans = min(ans,money)
if ans == 10**9:
    print(-1)
else:
    print(ans)