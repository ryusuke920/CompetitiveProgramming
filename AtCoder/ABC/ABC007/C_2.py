from  collections import deque
r, c = map(int,input().split())
sy, sx = map(int,input().split())
gy, gx = map(int,input().split())
s = [list(input().rstrip()) for _ in range(r)]

dist = [[10000] * c for _ in range(r)]
dist[sy - 1][sx - 1] = 0 # スタート地点だけ0に更新
for i in range(r):
    for j in range(c):
        if s[i][j] == '#':
            dist[i][j] = -1

q = deque()
q.append([sy - 1, sx - 1]) # 0index

d = [[0, -1], [0, 1], [-1, 0], [1, 0]]

while q:
    v = q.popleft() # y座標・x座標
    for i, j in d:
        if 0 <= v[1] + i <= c - 1 and 0 <= v[0] + j <= r - 1:
            if dist[v[0] + i][v[1] + j] != 10000: continue
            dist[v[0] + i][v[1] + j] = dist[v[0]][v[1]] + 1
            q.append([v[0] + i, v[1] + j])

print(dist[gy - 1][gx - 1])