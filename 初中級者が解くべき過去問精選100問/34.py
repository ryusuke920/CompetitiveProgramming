n = int(input())
dp = [0] * (n + 1)
(dp[0], dp[1]) = (1, 1)
def fibonacci(x):
    for i in range(2, x + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[x]

print(fibonacci(n))