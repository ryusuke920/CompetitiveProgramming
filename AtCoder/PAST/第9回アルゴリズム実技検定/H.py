s = input()
t = input()
l1 = len(s)
l2 = len(t)
# dp[i][j] := sのi文字目まで、tのj文字目までをみた時に作れる異なる最大値
# dp[i][j] = dp[i - 1][j]
dp = [[0] * (l1 + 1) for _ in range(l2 + 1)]
