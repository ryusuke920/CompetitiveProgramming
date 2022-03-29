n, m, K, s, t, x = map(int, input().split())
edge = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]
s -= 1
t -= 1
x -= 1

# dp[i][j][k] := 辺を i 回貼り、現在 j にいて、 X を k 回(偶奇)通った時の通り数
dp = [[[0] * 2 for _ in range(n + 1)] for _ in range(K + 1)]
dp[0][s][0] = 1

for i in range(K):
    for u, v in edge:
        for k in range(2):
            dp[i + 1][u][k] += dp[i][v][k ^ (v == x)]
            dp[i + 1][v][k] += dp[i][u][k ^ (u == x)]
            dp[i + 1][u][k] %= 998244353
            dp[i + 1][v][k] %= 998244353

print(dp[K][t][0])