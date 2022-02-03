n = int(input())

# dp[i][j] := i日目にjを選んだときの幸福度の最大値
dp = [[0] * 3 for _ in range(n + 1)]
for i in range(1, n + 1):
    a = list(map(int, input().split()))
    if i == 1:
        for j in range(3):
            dp[i][j] = a[j]
    else:
        for j in range(3):
            for k in range(3):
                if j == k: continue
                dp[i][k] = max(dp[i][k], dp[i - 1][j] + a[k])
#print(*dp,sep='\n')
print(max(dp[n]))