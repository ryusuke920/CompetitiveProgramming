n = int(input())
bank = [59049, 46656, 7776, 6561, 1296, 729, 216, 81, 36, 9, 6, 1]

dp = [10 ** 9] * (n + 1)
dp[0] = 0

for item in bank:
    for i in range(n + 1):
        if i + item <= n:
            dp[i + item] = min(dp[i] + 1, dp[i + item])

print(dp[n])