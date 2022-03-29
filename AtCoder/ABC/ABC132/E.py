from collections import deque

n, m = map(int, input().split())
edge = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]
s, t = map(lambda x: int(x) - 1, input().split())

g = [[] for _ in range(n)]
for u, v in edge:
    g[u].append(v)

# dist[i][j] := 頂点 i に mod 3 で j にたどり着ける最小手数
dist = [[-1] * 3 for _ in range(n)]
dist[s][0] = 0
q = deque()
q.append((s, 0)) # 頂点, 最短距離
while q:
    v, cnt = q.popleft()
    for i in g[v]:
        if dist[i][(cnt + 1) % 3] == -1:
            dist[i][(cnt + 1) % 3] = dist[v][cnt % 3] + 1
            q.append([i, dist[i][(cnt + 1) % 3]])

#print(*dist, sep='\n')
ans = 10 ** 18
for i in range(3):
    if dist[t][i] % 3 == 0:
        ans = min(ans, dist[t][i] // 3)

print(ans) if ans != 10 ** 18 else print(-1)