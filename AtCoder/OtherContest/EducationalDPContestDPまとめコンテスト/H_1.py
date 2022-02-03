h, w = map(int,input().split())
a = [list(input()) for _ in range(h)]

# dp[i][j] := i行j列目にいける組み合わせの数
dp = [[0] * (w + 1) for _ in range(h + 1)]
dp[1][1] = 1

mod = 10 ** 9 + 7
for i in range(h):
    for j in range(w):
        if a[i][j] == "#" or (i == 0 and j == 0): continue    
        dp[i + 1][j + 1] = (dp[i][j + 1] + dp[i + 1][j]) % mod

print(dp[h][w] % mod)