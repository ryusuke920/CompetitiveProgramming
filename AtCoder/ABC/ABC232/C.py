from itertools import permutations
from collections import defaultdict

n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]
cd = [list(map(int, input().split())) for _ in range(m)]

g1 = [[] for _ in range(n)]
for i in range(m):
    x, y = ab[i]
    x -= 1
    y -= 1
    g1[x].append(y)
    g1[y].append(x)

for i in range(n):
    g1[i].sort()

ans = False
for i in permutations([i for i in range(n)]):
    d = defaultdict(int)
    for j in range(n):
        d[j] = i[j]
    
    g2 = [[] for _ in range(n)]
    for j in range(m):
        x, y = cd[j]
        x -= 1
        y -= 1
        g2[d[x]].append(d[y])
        g2[d[y]].append(d[x])
    
    for j in range(n):
        g2[j].sort()

    bool = True
    for j in range(n):
        if g1[j] == g2[j]: continue
        bool = False
    
    if bool:
        ans = True

print('Yes') if ans else print('No')