n, K, p = map(int, input().split())
c = []
a = [[0] * 6 for _ in range(n)]
for i in range(n):
    s, *t = map(int, input().split())
    c.append(s)
    for j in range(len(t)):
        a[i][j] = t[j]

# print(c)
# print()
# print(*a, sep="\n")

INF = 10**18
dp = [[[[[[INF] * 6 for _ in range(6)] for _ in range(6)] for _ in range(6)] for _ in range(6)] for _ in range(101)]
dp[0][0][0][0][0][0] = 0
for num in range(n):
    for i in range(6):
        for j in range(6):
            for k in range(6):
                for l in range(6):
                    for m in range(6):
                        dp[num + 1][i][j][k][l][m] = min(dp[num + 1][i][j][k][l][m], dp[num][i][j][k][l][m])
                        ii = min(p, i + a[num][0])
                        jj = min(p, j + a[num][1])
                        kk = min(p, k + a[num][2])
                        ll = min(p, l + a[num][3])
                        mm = min(p, m + a[num][4])
                        # for _ in range(5):
                        #     t.append(min(p, i + a[num[_]]))
                        if dp[num][i][j][k][l][m] < INF:
                            dp[num + 1][ii][jj][kk][ll][mm] = min(dp[num + 1][ii][jj][kk][ll][mm], dp[num][i][j][k][l][m] + c[num])

idx = [0] * 6
for i in range(K):
    idx[i] = p

ans = dp[n][idx[0]][idx[1]][idx[2]][idx[3]][idx[4]]
print(-1) if ans == INF else print(ans)