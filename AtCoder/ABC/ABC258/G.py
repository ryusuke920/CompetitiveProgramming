from collections import defaultdict

n = int(input())
a = [list(map(int, input())) for _ in range(n)]
d = defaultdict(int)
g = [[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if a[i][j] == 1:
            g[i].append(j)

l = [0] * n
for i in range(n):
    l[i] = len(g[i])
    g[i].sort()
#print(*g, sep='\n')

for i in range(n):
    for j in range(l[i] - 1):
        for k in range(j + 1, l[i]):
            if i < g[i][j] < g[i][k]:
                d[f"{g[i][j]}_{g[i][k]}"] += 1

ans = 0

for i in range(n):
    for k in range(n):
        if a[i][k] == 0:
            continue
        ans += d[f'{i}_{k}']

print(ans)