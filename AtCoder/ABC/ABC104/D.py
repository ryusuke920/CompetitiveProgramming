s = input()
l = len(s)

mod = 10 ** 9 + 7
# dp[i][j] := i 番目までで状態が j まで決まっている時の通り数
# i 番目が
dp = [[0] * 4 for _ in range(l + 1)]
dp[0][0] = 1

for i in range(l):
    for j in range(4):
        if s[i] == '?':


print(dp[-1][3])