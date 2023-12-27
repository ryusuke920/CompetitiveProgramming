def solve():

    dp[0][0][0][0][0][0] = 0

    for i in range(N):
        for j in range(6):
            for k in range(6):
                for l in range(6):
                    for m in range(6):
                        for n in range(6):
                            dp[i + 1][j][k][l][m][n] = min(dp[i + 1][j][k][l][m][n], dp[i][j][k][l][m][n])

                            i2 = min(P, j + A[i][0])
                            j2 = min(P, k + A[i][1])
                            k2 = min(P, l + A[i][2])
                            l2 = min(P, m + A[i][3])
                            m2 = min(P, n + A[i][4])

                            if dp[i][j][k][l][m][n] < INF:
                                dp[i + 1][i2][j2][k2][l2][m2] = min(dp[i + 1][i2][j2][k2][l2][m2], dp[i][j][k][l][m][n] + C[i])

    idx = [0] * 6
    for i in range(K):
        idx[i] = P
    ans = dp[N][idx[0]][idx[1]][idx[2]][idx[3]][idx[4]]
    
    if ans > 1e16:
        ans = -1
    
    print(ans)

if __name__ == "__main__":
    N, K, P = map(int, input().split())
    C = []
    A = [[0] * 6 for _ in range(N)]
    
    for i in range(N):
        s, *t = map(int, input().split())
        C.append(s)
        for j in range(K):
            A[i][j] = t[j]
    INF = 10**18
    dp = [[[[[[INF for _ in range(6)] for _ in range(6)] for _ in range(6)] for _ in range(6)] for _ in range(6)] for _ in range(101)]
    
    solve()
