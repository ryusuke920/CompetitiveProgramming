# warshall_floyd法
def warshall_floyd():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

INF = 10 ** 20
n, m = map(int,input().split())

dist = [[INF] * n for _ in range(n)]

v = [list(map(int, input().split())) for _ in range(m)]

for a, b, c in v:
    dist[a - 1][b - 1] = c
    dist[b - 1][a - 1] = c

warshall_floyd()

ans = 0
for a, b, c in v:
    for i in range(n):
        if dist[a - 1][i] + dist[i][b - 1] <= c:
            ans += 1
            break

print(ans)