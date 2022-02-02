n,w = map(int,input().split())
dp = [[0] * 10010 for _ in range(110)]
value = [0] * 110
weight = [0] * 110
for i in range(n):
    value[i], weight[i] = map(int,input().split())
for i in range(n):
    for j in range(w + 1): # jに重りの価値を追加する 
        if j >= weight[i]:
            dp[i + 1][j] = max(dp[i][j - weight[i]] + value[i], dp[i][j])
        else:
            dp[i + 1][j] = dp[i][j]
print(dp[n][w])