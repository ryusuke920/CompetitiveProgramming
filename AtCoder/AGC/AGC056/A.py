n = int(input())

grid = [["."] * n for _ in range(n)]
for i in range(n):
    for j in range(3 * i, 3 * (i + 1)):
        grid[i][j % n] = "#"

if n % 3:
    for i in range(n):
        grid[0][i], grid[n // 3][i] = grid[n // 3][i], grid[0][i]

    for i in range(n):
        grid[-1][i], grid[-n // 3][i] = grid[-n // 3][i], grid[-1][i]

for i in grid:
    print(*i, sep="")