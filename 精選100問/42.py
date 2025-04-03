import sys
input = sys.stdin.readline
n, m = map(int,input().split()) # 都市の数、制限日数
d = [int(input()) for _ in range(n)] # 都市を結ぶ距離
c = [int(input()) for _ in range(m)] # 天候の悪さ( >= 1 )
INF = 10 ** 18
dp = [[INF] * (m + 1) for _ in range(n + 1)] # dp[i][j] := i日目までにj番目の都市に来た時の最小コスト

for i in range(m + 1):
    dp[0][i] = 0 # 都市0は便宜上０

for i in range(n): # 都市
    for j in range(m): # 天候
        dp[i + 1][j + 1] = min(dp[i][j] + d[i] * c[j], dp[i + 1][j])
print(dp[-1][-1])