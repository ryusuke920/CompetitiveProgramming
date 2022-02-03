n, m , q = map(int,input().split())
l, r = [0] * m, [0] * m
h, w = 0, 0
for i in range(m):
    l[i], r[i] = map(int,input().split())
    h, w = max(h, l[i] + 1), max(w, r[i] + 1)

# 二次元累積和
# grid[i][j] := iからjへの電車が通っている
grid = [[0] * w for _ in range(h)]
for i in range(m):
    grid[l[i]][r[i]] += 1

for i in range(h - 1):
    for j in range(w):
        grid[i + 1][j] += grid[i][j]

for i in range(h):
    for j in range(w - 1):
        grid[i][j + 1] += grid[i][j]

for i in range(q):
    p, q = map(int,input().split())
    S = grid[h - 1][q] - grid[min(p - 1, h - 1)][q]
    print(S)