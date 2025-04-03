from itertools import product
n,m = map(int,input().split())
ks = [list(map(int,input().split())) for _ in range(m)]
p = list(map(int,input().split()))
ans = 0
for tpl in product([0,1], repeat = n):
    bl = True
    for i in range(m):
        x = [tpl[j-1] for j in ks[i][1:]]
        x = sum(x)
        if x%2 != p[i]:
            bl = False
    if bl:
        ans += 1
print(ans)