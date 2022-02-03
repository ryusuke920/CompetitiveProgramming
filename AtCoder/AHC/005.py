import sys
input = sys.stdin.readline
from collections import deque

n, sy, sx = map(int,input().split())

grid = [list(input()) for _ in range(n)]

INF = 10 ** 18
dist = [[INF] * n for _ in range(n)]
dist[sy][sx] = 0

q = deque()
q.append((sy, sx))
d = ((0, 1), (0, -1), (1, 0), (-1, 0))

already_pos = set()
already_pos.add((sy, sx))

while q:
    vy, vx = q.popleft()
    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        y, x = dy + vy, dx + vx
        if not (0 <= y < n and 0 <= x < n): continue
        if grid[y][x] == '#': continue
        if dist[y][x] != INF: continue
        dist[y][x] = dist[vy][vx] + 1
        q.append((y, x))
        already_pos.add((y, x))

#print(*dist,sep="\n")

ma = 0
end_sy, end_sx = 0, 0
for i in range(n):
    for j in range(n):
        if ma < dist[i][j] and dist[i][j] != INF:
            ma = dist[i][j]
            end_sy, end_sx = i, j

#print(ma, end_sy, end_sx)
    
ans = ""
d = ((0, 1, "R"), (0, -1, "L"), (1, 0, "D"), (-1, 0, "U"))

while ma > 0:
    cnt = 0 # ４方向のどこにいけるか
    for dy, dx, direct in d:
        y = end_sy + dy
        x = end_sx + dx
        if not (0 <= y < n and 0 <= x < n): continue
        if dist[y][x] == ma - 1 and (y, x) not in already_pos:    
            ma -= 1
            ans += direct
            end_sy = y
            end_sx = x
            break
        elif dist[y][x] == ma - 1:
            ma -= 1
            ans += direct
            end_sy = y
            end_sx = x
            break

#print(ans)

reverse_ans = ""
for dire in ans:
    if dire == "U":
        reverse_ans += "D"
    elif dire == "D":
        reverse_ans += "U"
    elif dire == "L":
        reverse_ans += "R"
    elif dire == "R":
        reverse_ans += "L"

print(reverse_ans[::-1] + ans)