n = int(input())
from collections import defaultdict
from math import gcd
d = defaultdict(int)
xy = [list(map(int,input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j: continue
        yy = xy[j][1]
        y = xy[i][1]
        xx = xy[j][0]
        x = xy[i][0]
        flag = [False] * 2
        
        s = yy - y
        t = xx - x

        if s < 0:
            flag[0] = True
            s *= -1
        if t < 0:
            flag[1] = True
            t *= -1
        
        num = gcd(s, t)
        s //= num
        t //= num
        if flag[0]:
            s *= -1
        if flag[1]:
            t *= -1

        u = f"{s}_{t}"
        if d[u] == 0:
            d[u] += 1

print(len(d))