def f(a: int, b: int) -> bool:
    if a == b:
        return 0
    if (a == 'R' and b == 'S') or (a == 'S' and b == 'P') or (a == 'P' and b == 'R'):
        return 1
    return -1


N = int(input())
S = input()
x = "RPS"
dp = [[0] * 3 for _ in range(N + 1)]
for i in range(N):
    for j in range(3):
        for k in range(3):
            # 同じならスルー
            if x[j] == x[k]:
                continue
            if f(x[k], S[i]) == -1:
                continue
            dp[i + 1][k] = max(dp[i + 1][k], dp[i][j] + f(x[k], S[i]))

print(max(dp[N]))