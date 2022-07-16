# warshall_floyd法
def warshall_floyd() -> list:
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

INF = 10 ** 20
n = int(input())
s = [int(input()) for _ in range(n)]

dist = [[INF] * n for _ in range(n)] # 隣接行列の初期化

# 自分自身へのコストは 0
for i in range(n):
    dist[i][i] = 0

# 与えられた距離の初期化
for i in range(m):
    x, y, r = map(int,input().split())
    dist[x][y] = r
    dist[y][x] = r

ans = warshall_floyd()
print(*ans, sep='\n')