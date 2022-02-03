h, w, c = map(int,input().split())
a = [list(map(int,input().split())) for _ in [0] * h]
INF = 10 ** 18
ans = INF

for _ in range(2):
    dp = [[INF] * w for _ in [0] * h]
    dp[0][0] = a[0][0]
    for i in range(h):
        for j in range(w):
            if i != 0:
                ans = min(ans, dp[i - 1][j] + c + a[i][j])
                dp[i][j] = min(a[i][j], dp[i][j], dp[i - 1][j] + c)
            if j != 0:
                ans = min(ans, dp[i][j - 1] + c + a[i][j])
                dp[i][j] = min(a[i][j], dp[i][j], dp[i][j - 1] + c)

    a = [i[::-1] for i in a]

print(ans)
#ガチでわからんなんなんこれまじで