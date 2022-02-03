n = int(input())
t = list(map(int, input().split()))
l = 10 ** 5 + 1
dp = [[False] * l for _ in range(n + 1)]
# dp[i][j] := i番目までの品で合計時間をj分にできるか
dp[0][0] = True
for i in range(n):
    for j in range(l):
        if j - t[i] >= 0:
            dp[i + 1][j] |= dp[i][j - t[i]]
        dp[i + 1][j] |= dp[i][j]

ans = 10 ** 18
time = sum(t)
for i in range(l):
    if dp[-1][i]:
        ans = min(ans, max(i, time - i))
print(ans)