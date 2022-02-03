n, W = map(int,input().split())
w, v = [0] * n, [0] * n
for i in range(n):
    w[i], v[i] = map(int,input().split())
"""
各価値について、最小の重さを求める方針でやっていく
価値の総和は0 <= value <= 10 ** 5 (<- 10 ** 3 * N)
最後に逆で見ていくと答え出る
具体的には、
10 ** 5の価値の重さの最小値はW以下ですか？ -> No
10 ** 5 - 1の価値の重さの最小値はW以下ですか？ -> No
10 ** 5 - 2の価値の重さの最小値はW以下ですか？ -> No
...
...
10 ** 5 - xの価値の重さの最小値はW以下ですか？ -> Yes
これが答え！！！みたいな方針

dp[i][j] := i番目までの品物で、価値の総和がjの時の最小となる重さWの値
"""

INF = 10 ** 18
dp = [[INF] * (10 ** 5 + 1) for _ in range(n + 1)]
dp[0][0] = 0

for i in range(n):
    for j in range(10 ** 5 + 1):
        if j - v[i] >= 0: # i番目の物を足すとき
            dp[i + 1][j] = min(dp[i][j], dp[i][j - v[i]] + w[i])
        else:
            dp[i + 1][j] = dp[i][j]

# 後ろから答えを見つける
for i in reversed(range(10 ** 5 + 1)):
    if dp[n][i] <= W:
        exit(print(i))