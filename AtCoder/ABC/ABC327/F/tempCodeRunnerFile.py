n = int(input())
p = list(map(int, input().split()))

INF = 10**18
# dp[i][j] := i 番目のコンテストを j 個目で選んだ時のレートの最大値
dp = [[-INF] * (n + 1) for _ in range(n + 1)]
for i in range(n):
    dp[i + 1][1] = p[i]

under = [0] * (n + 1)
under[1] = 1
for i in range(2, n + 1):
    under[i] = under[i - 1] * 0.9 + 1
#print(under)

for i in range(2, n + 1):
    for j in range(2, i + 1):
        #print(i, j,p[i-1])
        dp[i][j] = max(dp[i][j], dp[i - 1][j]) # 選ばない
        # 選ぶ
        t = dp[i - 1][j - 1] * under[j - 1] * 0.9 + p[i - 1]
        s = under[j]
        #print(i, j, t, s, dp[i - 1][j - 1] * 0.9 + p[i-1])
        dp[i][j] = max(dp[i][j], t / s)


ans = -INF
for i in range(1, n + 1):
    ans = max(ans, dp[n][i] - 1200/(i**0.5))

#print(*dp, sep="\n")
print(ans)
print(711,1200/1.7320508)