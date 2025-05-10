from collections import deque
H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
dist = [[-1]*W for _ in range(H)]
q = deque()
for i in range(H):
    for j in range(W):
        if S[i][j] == "E":
            dist[i][j] = 0
            q.append((i, j))

d = ((-1, 0), (1, 0), (0, 1), (0, -1))
while q:
    vy, vx = q.popleft()
    for dy, dx in d:
        ny = vy + dy
        nx = vx + dx
        if not (0 <= ny < H and 0 <= nx < W):
            continue
        if dist[ny][nx] != -1:
            continue
        if S[ny][nx] == "#":
            continue
        dist[ny][nx] = dist[vy][vx] + 1
        q.append((ny, nx))

ans = [[""]*W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            ans[i][j] = "#"
        elif S[i][j] == "E":
            ans[i][j] = "E"
        else:
            for dy, dx, arrow_ in ((-1, 0, "v"), (1, 0, "^"), (0, 1, ">"), (0, -1, "<")):
                ny = i + dy
                nx = j + dx
                if not (0 <= ny < H and 0 <= nx < W):
                    continue
                if dist[ny][nx] + 1 == dist[i][j]:
                    if dy == 1 and dx == 0:
                        ans[i][j] = "v"
                    elif dy == -1 and dx == 0:
                        ans[i][j] = "^"
                    elif dy == 0 and dx == 1:
                        ans[i][j] = ">"
                    elif dy == 0 and dx == -1:
                        ans[i][j] = "<"
                    break

for i in range(H):
    print(*ans[i], sep="")