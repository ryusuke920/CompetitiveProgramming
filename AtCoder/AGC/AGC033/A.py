from collections import deque
import sys
input = sys.stdin.readline
h, w = map(int,input().split())
grid = []
q = deque()
dist = [[10 ** 9] * w for _ in range(h)]
for i in range(h):
    a = list(input())
    grid.append(a)
    for j in range(w):
        if a[j] == "#":
            dist[i][j] = 0 # スタート地点は0
            q.append([i, j]) # 0index

d = [[0, 1], [0, -1], [1, 0], [-1, 0]] # 上下左右への変化量
while q:
    v = q.popleft()
    for i, j in d:
        if not (0 <= v[0] + i <= h - 1 and 0 <= v[1] + j <= w - 1): continue
        if dist[v[0] + i][v[1] + j] <= dist[v[0]][v[1]] + 1: continue
        dist[v[0] + i][v[1] + j] = dist[v[0]][v[1]] + 1
        q.append([v[0] + i, v[1] + j])

ans = 0
for i in range(h):
    ans = max(ans, max(dist[i]))
print(ans)