# warshall_floyd法
def warshall_floyd(d):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j]= min(d[i][j], d[i][k] + d[k][j])
    return d

n, m, l = map(int,input().split())

# 隣接行列の初期化
g = [[float('inf')] * n for _ in range(n)]
# 自分自身へのコストは０
for i in range(n):
    g[i][i] = 0

# コストを入力
for i in range(m):
    a, b, c = map(int,input().split())
    g[a - 1][b - 1] = c
    g[b - 1][a - 1] = c

dist = warshall_floyd(g)
new_dist = [[float('inf')] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j: continue
        if dist[i][j] <= l:
            new_dist[i][j] = 1
            new_dist[j][i] = 1

print(*new_dist, sep = "\n")
ans = warshall_floyd(new_dist)
print(*ans,sep = "\n")

q = int(input()) # クエリ数
for i in range(q):
    s, t = map(int,input().split())
    if ans[s - 1][t - 1] == float('inf'):
        print(-1)
    else:
        print(ans[s - 1][t - 1] - 1)