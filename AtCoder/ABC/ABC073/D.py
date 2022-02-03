from itertools import permutations

# warshall_floyd法
def warshall_floyd(d):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d

INF = 10 ** 20
n, m, r = map(int,input().split()) # 頂点数・辺の数
t = list(map(int,input().split()))

d = [[INF] * n for _ in range(n)] # 隣接行列の初期化

# 自分自身へのコストは0
for i in range(n):
    d[i][i] = 0

# 与えられた距離の初期化
for i in range(m):
    x, y, r = map(int,input().split())
    d[x - 1][y - 1] = r
    d[y - 1][x - 1] = r

# sからtへの最短距離を求める
dist = warshall_floyd(d)

ans = INF
for i in permutations(t):
    cost = 0
    for j in range(len(t) - 1):
        cost += dist[i[j] - 1][i[j + 1] - 1]
    ans = min(ans, cost)

print(ans)