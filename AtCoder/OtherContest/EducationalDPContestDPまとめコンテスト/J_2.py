n = int(input())
a = list(map(lambda x: int(x) - 1, input().split()))

# dp[i][j][k] := [1,2,3]枚の皿が残り[i,j,k]枚の時の全ての寿司を無くすまでの期待値
dp = [[[0] * (n + 1) for _ in range(n + 1)] for _ in range(n + 1)]

# 皿の枚数を計算する
cnt = [0] * 3
for i in range(n):
    cnt[a[i]] += 1

for k in range(n + 1):
    for j in range(n + 1):
        for i in range(n + 1):
            p = i + j + k
            if p == 0 or p > n:
                continue
            prob = 0
            if i >= 1:
                prob += dp[i - 1][j][k] * i
            if j >= 1:
                prob += dp[i + 1][j - 1][k] * j
            if k >= 1:
                prob += dp[i][j + 1][k - 1] * k
            prob += n

            dp[i][j][k] += (prob / p)

x, y, z = cnt
print(dp[x][y][z])