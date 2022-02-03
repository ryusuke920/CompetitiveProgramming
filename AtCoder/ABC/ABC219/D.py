import sys
input = sys.stdin.readline

n = int(input())
x, y = map(int,input().split())
ab = [list(map(int,input().split())) for _ in range(n)]

INF = 10 ** 18
num = 301
dp = [[[INF] * num for _ in range(num)] for _ in range(n + 1)]
# dp[i][j][k] := i番目までの商品でたこ焼きの合計がj上, たい焼きがk以上となる最小の弁当の個数
for i in range(n + 1):
    dp[i][0][0] = 0

for i in range(n):
    for j in range(num):
        for k in range(num):
            # 弁当を買える場合
            dp[i + 1][j][k] = dp[i][max(0, j - ab[i][0])][max(0, k - ab[i][1])] + 1
            dp[i + 1][j][k] = min(dp[i][j][k], dp[i + 1][j][k])

ans = INF
for i in range(x, num):
    for j in range(y, num):
        ans = min(ans, dp[n][i][j])

if ans == INF:    
    print(-1)
else:
    print(ans)