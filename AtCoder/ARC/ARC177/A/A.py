N = int(input())
A = list(map(int, input().split()))

mod = 998244353
# dp[i][S] := i 番目までのサイコロで集合 S で 10 を作れる確率
dp = [[0]*(1 << 11) for _ in range(N + 1)]
dp[0][1] = 1
for i in range(N):
    p = pow(A[i], -1, mod)
    for S in range(1 << 11):
        for j in range(1, min(11, A[i] + 1)):
            dp[i + 1][(S | (S << j)) & ((1 << 11) - 1)] += dp[i][S] * p
        if A[i] >= 11:
            dp[i + 1][S] += dp[i][S] * max(0, A[i] - 10) * p
        dp[i + 1][S] %= mod

ans = 0
for i in range(1 << 11):
    if (i >> 10):
        ans += dp[N][i]
    ans %= mod
print(ans)