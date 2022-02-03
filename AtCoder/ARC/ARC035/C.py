import sys
input = sys.stdin.readline

# warshall_floyd法
def warshall_floyd(d):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d
INF = 10 ** 9
n, m = map(int,input().split())

d = [[INF] * n for _ in range(n)]

for i in range(n):
    d[i][i] = 0

for _ in range(m):
    a, b, c = map(int,input().split())
    d[a - 1][b - 1] = c
    d[b - 1][a - 1] = c

# sからtへの最短距離を求める
dist = warshall_floyd(d)

k = int(input())
for _ in range(k):
    x, y, z = map(int,input().split())
    for i in range(n - 1):
        for j in range(i + 1, n):
            if i == j: continue
            dist[i][j] = min(dist[i][j], dist[i][x - 1] + dist[y - 1][j] + z, dist[i][y - 1] + dist[j][x - 1] + z)
            dist[j][i] = dist[i][j]

    ans = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            ans += dist[i][j]
    
    print(ans)