from collections import deque
h, w = map(int,input().split())
ch, cw = map(int,input().split())
dh, dw = map(int,input().split())
ch, cw, dh, dw = ch - 1, cw - 1, dh - 1, dw - 1 # 0index
s = [list(input()) for _ in range(h)]
INF = 10 ** 18
dist = [[INF] * w for _ in range(h)]

q = deque()
q.append((ch, cw)) # y座標・x座標
dist[ch][cw] = 0

# 周囲25マスの生成
d = set()
for i in range(-2, 3):
    for j in range(-2, 3):
        d.add((i, j))

while q:
    vy, vx = q.popleft() # 今いる場所のy座標・x座標

    for dy, dx in d:
        cnt = abs(dy) + abs(dx) >= 2 # 1 -> 魔法を使う, 0 -> 魔法を使わない (上下左右に移動する <=> コストはかからない)
        if not (0 <= vy + dy <= h - 1 and 0 <= vx + dx <= w - 1): continue
        if dist[vy + dy][vx + dx] <= dist[vy][vx] + cnt: continue
        if s[vy + dy][vx + dx] == ".":
            dist[vy + dy][vx + dx] = dist[vy][vx] + cnt

            if cnt == 0:
                q.appendleft((vy + dy, vx + dx))
            elif cnt == 1:
                q.append((vy + dy, vx + dx))

if dist[dh][dw] == INF:
    print(-1)
else:
    print(dist[dh][dw])