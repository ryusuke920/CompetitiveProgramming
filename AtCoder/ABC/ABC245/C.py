n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = []
for i, j in zip(a, b):
    c.append([i, j])

# dp[i][j] := Xi に　 (Aj, Bj) から (Al, Bl) に遷移できるかどうか
dp = [[False] * 2 for _ in range(n + 1)]
dp[1][0] = True
dp[1][1] = True
for i in range(2, n + 1):
    for j in range(2):
        for l in range(2):
            if dp[i - 1][j]:
                if abs(c[i - 2][j] - c[i - 1][l]) <= k:
                    dp[i][l] |= True

print('Yes') if dp[n][0] or dp[n][1] else print('No')