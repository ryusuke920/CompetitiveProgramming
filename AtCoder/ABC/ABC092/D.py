A, B = map(int, input().split())
A, B = B, A
H, W = 100, 100
grid = [["#"]*W for _ in range(H)]

for i in range(H // 2):
    for j in range(W):
        grid[i + H // 2][j] = "."

A -= 1
B -= 1
ny, nx = 1, 1
while B > 0:
    grid[ny][nx] = "."
    nx += 2
    if nx >= W:
        nx = 2
        ny += 2
    B -= 1

ny, nx = H // 2 + 1, 1
while A > 0:
    grid[ny][nx] = "#"
    nx += 2
    if nx >= W:
        nx = 2
        ny += 2
    A -= 1

print(H, W)
for i in range(H):
    print(*grid[i], sep="")