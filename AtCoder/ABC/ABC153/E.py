import sys
input = sys.stdin.readline
h, n = map(int,input().split())
ab = [list(map(int,input().split())) for _ in range(n)] # 減らせる体力・魔力
INF = 10 ** 18
ma = 0 # 配列Aの最大値
for i in range(n):
    ma = max(ma, ab[i][0])

dp = [INF] * (h + ma + 1) # dp[i] := i与える時の最小魔力
dp[0] = 0
for i in range(h + ma):
    for attack, damage in ab:
        dp[i + 1] = min(dp[i + 1], dp[i + 1 - attack] + damage)

ans = INF
dp = dp[h:]
for i in range(len(dp)):
    ans = min(ans, dp[i])

print(ans)