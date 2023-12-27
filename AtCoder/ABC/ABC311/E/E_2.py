h, w, n = map(int, input().split())

s = set()
for _ in range(n):
    a, b = map(lambda x: int(x) - 1, input().split())
    s.add(a * 3000 + b)

dp = [[0] * w for _ in range(h)]
ans = 0
for i in range(h):
    for j in range(w):
        if i * 3000 + j not in s:
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        ans += dp[i][j]

print(ans)