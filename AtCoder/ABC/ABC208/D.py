INF = 10 ** 20
n, m = map(int,input().split()) # 頂点数・辺の数
d = [[INF] * n for _ in range(n)] # 隣接行列の初期化

# 自分自身へのコストは0
for i in range(n):
    d[i][i] = 0

# 与えられた距離の初期化
for i in range(m):
    x, y, r = map(int,input().split())
    d[x - 1][y - 1] = r

ans = 0
# warshall_floyd法
for k in range(n):
    for i in range(n):
        for j in range(n):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])
            if d[i][j] != INF and i != j:
                ans += d[i][j]

print(ans)