n = int(input())
grid = [input() for _ in range(5)]

color = [[5] * 3 for _ in range(n)]
for i in range(n):
    for j in range(5):
        if grid[j][i] == "R":
            color[i][0] -= 1
        elif grid[j][i] == "B":
            color[i][1] -= 1
        elif grid[j][i] == "W":
            color[i][2] -= 1

dp = [[0] * 3 for _ in range(n)] # 列 * (赤・青・白)
dp[0] = color[0]
for i in range(n - 1):
    for j in range(3): # 3色
        dp[i + 1][j] = min(dp[i][j - 1], dp[i][j - 2]) + color[i + 1][j]

print(min(dp[-1]))