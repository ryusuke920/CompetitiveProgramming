n = int(input())
s = input()

# dp[i][j] := i番目までの文字で今見てるのかアルファベットjである時の作れる状態数
dp = [[0] * 10 for _ in range(n + 1)]
mod = 998244353

for i in range(n):
    for j in range(10):    
        dp[i + 1][j] += sum(dp[i])
    for j in range(10):
        dp[i + 1][j] %= mod

print(*dp, sep= "\n")