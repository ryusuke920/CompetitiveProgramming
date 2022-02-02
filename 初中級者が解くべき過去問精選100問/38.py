import sys
input = sys.stdin.readline
q = int(input().rstrip())
for i in range(q):
    s = input().rstrip()
    t = input().rstrip()
    # dp[i][j] := sのi番目、tのj番目までで作れる最大共通部分列文字列
    dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
    for i in range(len(s)):
        for j in range(len(t)):
            if s[i] == t[j]:
                dp[i + 1][j + 1] = max(dp[i][j] + 1, dp[i + 1][j], dp[i][j + 1])
            else:
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
    print(dp[len(s)][len(t)])