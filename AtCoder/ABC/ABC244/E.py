n, m, k, s, t, x = map(int, input().split())
edge = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]

# dp[i][j][k] := S からスタートして、辺を i 回貼り、　現在 j にいて、 X を k（偶奇） 回通った場合の通り数
dp = [[[0] * 2 for _ in range(n + 1)] for _ in range(k + 1)]
dp[0][s - 1][0] = 1

for i in range(k):
    for u, v in edge:
        for bit in range(2):
            dp[i + 1][u][bit] += dp[i][v][bit ^ (v == x - 1)]
            dp[i + 1][v][bit] += dp[i][u][bit ^ (u == x - 1)]
            dp[i + 1][u][bit] %= 998244353
            dp[i + 1][v][bit] %= 998244353

print(dp[-1][t - 1][0])