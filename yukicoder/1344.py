# warshall_floyd法
def warshall_floyd() -> list:
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

INF = float('inf')
n, m = map(int,input().split()) # 頂点数・辺の数

dist = [[INF] * n for _ in range(n)] # 隣接行列の初期化

# 自分自身へのコストは 0
for i in range(n):
    dist[i][i] = 0

# 与えられた距離の初期化
for i in range(m):
    x, y, r = map(int,input().split())
    dist[x - 1][y - 1] = min(dist[x - 1][y - 1], r)

ans = warshall_floyd()

for i in range(n):
    num = 0
    for j in range(n):
        if i != j and ans[i][j] < INF:
            num += ans[i][j]
    print(num)