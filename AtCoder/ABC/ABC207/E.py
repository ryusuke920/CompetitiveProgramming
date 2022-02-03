n = int(input())
a = list(map(int,input().split()))
s = [0] * (n + 1)
for i in range(n):
    s[i + 1] = s[i] + a[i]
memo = [[0] * (n + 1) for i in range(n + 1)]
dp = [[0] * (n + 1) for i in range(n + 1)]
memo[1][0] = dp[0][0] = 1
mod = 10 ** 9 + 7

for i in range(n):
    for j in range(1, n + 1):
        dp[i + 1][j] = memo[j][s[i + 1] % j]
    for j in range(2, n + 1):
        memo[j][s[i + 1] % j] += dp[i + 1][j - 1]
        memo[j][s[i + 1] % j] %= mod

print(sum(dp[n]) % mod)