n = int(input())
d = [int(input()) for _ in range(n)]
mod = 10 ** 9 + 7
dp = [[0] * 4 for _ in range(n + 1)]
# dp[i][j] := i番目までの問題でj問目までを作成できる通り数
dp[0][0] = 1

