import sys
input = sys.stdin.readline
INF = 10 ** 18
# 入力
d, n = map(int,input().split()) # 日数、服の種類数
t = [0] * d # i日目の最高気温
for i in range(d):
    t[i] = int(input())
a, b, c = [0] * n, [0] * n, [0] * n
for i in range(n):
    a[i], b[i], c[i] = map(int,input().split()) # 最高気温の最低、最高、派手度

dp = [[-INF] * (n + 1) for _ in range(d + 1)] # dp[i][j] := i日目にjの服を来た時の最大スコア

for i in range(d): # 日数
    for j in range(n): # i日目に着る服
        if a[j] <= t[i] <= b[j]: # i日目に服が着れる時
            if i == 0:
                dp[i + 1][j] = 0 # 着るやつないよ
                continue
            for k in range(n): # i - 1日目に着る服
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][k] +  abs(c[k] - c[j]))

print(max(dp[-1])) # 最終日の最大スコアを出力