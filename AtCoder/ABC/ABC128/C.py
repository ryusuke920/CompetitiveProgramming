n,m = map(int,input().split())
sw = [[]for _ in range(m)]
for i in range(m):
    sw[i] = list(map(int,input().split()[1:]))
p = list(map(int,input().split()))
import itertools
ans = 0
for i in itertools.product([0,1], repeat = n):
    bl = True
    for i in range(m):
        #電球iを計算
        s = sum([i[s-1] for _ in sw[i]])
        if (s-p[i])%2 != 0:
            bl = False
            break
    if bl:
        ans += 1
print(ans)