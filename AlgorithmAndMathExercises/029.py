n = int(input())

if n == 1:
    exit(print(1))

# dp[i] := i段目まで辿り着く通り数
dp = [0] * (n + 1)
dp[1] = 1
dp[2] = 2
for i in range(3, n + 1):
    dp[i] += dp[i - 1] + dp[i - 2]

print(dp[n])