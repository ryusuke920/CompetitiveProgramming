n, m = map(int,input().split())
from collections import defaultdict
a, b = [0] * m, [0] * m
for i in range(m):
    a[i], b[i] = map(int,input().split())
INF = 10 ** 18
ans = 0
c, d = [0] * m, [0] * m
for i in range(m):
    c[i], d[i] = a[i] - b[i], b[i] - a[i]

l = []
for i in range(m):
    l.append((a[i], b[i], c[i], d[i]))

l.sort(key = lambda x: (x[2], x[0], x[1]))

Bool = [[True] * 2 for _ in range(n)]
cnt = 0
for i in range(m):
    if Bool[l[i][0] - 1][0] and Bool[l[i][1] - 1][1]:
        cnt += 1
        Bool[l[i][0] - 1][0] = False
        Bool[l[i][1] - 1][1] = False
    else:
        break

ans = max(ans, cnt)

l.sort(key = lambda x: (x[3], x[0], x[1]))

Bool = [[True] * 2 for _ in range(n)]
cnt = 0
for i in range(m):
    if Bool[l[i][0] - 1][0] and Bool[l[i][1] - 1][1]:
        cnt += 1
        Bool[l[i][0] - 1][0] = False
        Bool[l[i][1] - 1][1] = False
    else:
        break

ans = max(ans, cnt)
print(n - ans)