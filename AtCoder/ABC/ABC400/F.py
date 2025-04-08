N = int(input())
C = [int(x) - 1 for x in input().split()]
C = C*2
X = [int(x) for x in input().split()]
inf = 10**18

ans = inf

dp = [[inf] * (2*N + 1) for _ in range(2*N + 1)]
dp2 = [[inf] * (2*N + 1) for _ in range(2*N + 1)]

for i in range(2*N + 1):
    for j in range(i + 1):
        dp[i][j] = 0
        dp2[i][j] = 0
    if i < 2*N:
        dp[i][i + 1] = X[C[i]] + 1
        dp2[i][i + 1] = 0

for s in range(1, N + 1):
    for l in range(2*N - s + 1):
        for m in range(l, l + s):
            dp2[l][l + s] = min(dp2[l][l + s], dp2[l][m] + dp[m][l + s])
            dp[l][l + s] = min(dp[l][l + s], dp[l][m] + dp[m][l + s])
        if C[l] == C[l + s - 1]:
            dp2[l][l + s] = min(dp2[l][l + s], dp2[l][l + s - 1])
            dp[l][l + s] = min(dp[l][l + s], dp2[l][l + s] + s + X[C[l]])

for i in range(N):
    ans = min(ans, dp[i][i + N])

print(ans)