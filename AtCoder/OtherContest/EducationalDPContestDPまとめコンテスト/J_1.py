n = int(input())
a = list(map(int,input().split()))

# １枚の皿、２枚の皿、３枚の皿が何皿ずつあるかを記録する
num = [0, 0, 0]
for i in a:
    num[i - 1] += 1

# dp[i][j][k] := １枚の皿がi枚、２枚の皿がj枚、３枚の皿がk枚残っているときの期待値
dp = [[[0] * (n + 1) for _ in range(n + 1)] for _ in range(n + 1)]

for k in range(n + 1):
    for j in range(n + 1):
        for i in range(n + 1):
            t = i + j + k
            # 皿がなかったり、N枚以上あればスルー
            if t == 0 or n < t: continue
            cnt = n
            if i >= 1:
                cnt += i * (dp[i - 1][j][k])
            if j >= 1:
                cnt += j * (dp[i + 1][j - 1][k])
            if k >= 1:
                cnt += k * (dp[i][j + 1][k - 1])

            dp[i][j][k] = 1 / t * cnt

X, Y, Z = num
print(dp[X][Y][Z])