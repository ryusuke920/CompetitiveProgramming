from collections import defaultdict
n, x = map(int, input().split())

dp = defaultdict(int)
dp[1] = 1

for i in range(n):
    l, *a = map(int, input().split())
    dp2 = defaultdict(int)
    for k, v in dp.items():
        for j in a:
            dp2[j * k] += v
    dp = dp2

print(dp[x])