h, w = map(int, input().split())
s = [[*input()] for _ in range(h)]

#左上から時計回り
dy = [-1, -1, -1, 0, 1, 1, 1, 0]
dx = [-1, 0, 1, 1, 1, 0, -1, -1]

for i in range(h):
    for j in range(w):
        if s[i][j] == "#": continue
        cnt = 0
        for k in range(8):
            x = j + dx[k]
            y = i + dy[k]
            if x < 0 or y < 0 or w <= x or h <= y: continue
            if s[y][x] == "#":
                cnt += 1
        s[i][j] = str(cnt)
print(*map("".join, s), sep = "\n")