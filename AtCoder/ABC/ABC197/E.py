n = int(input())
INF = 10 ** 18
l, r = [INF] * (n + 1), [-INF] * (n + 1)
l[0], r[0] = 0, 0
for _ in range(n):
    x, c = map(int,input().split())
    l[c] = min(l[c], x)
    r[c] = max(r[c], x)

# dp[i][j] := 色iのボールのうち、j = 0なら一番左、j = 1なら一番右のものと同じ位置にいて、
# 色iのボールは全て回収し終わった状態になるまでの最小の時間
dp = [[0] * 2 for _ in range(n + 1)]
x, y = 0, 0
for i in range(n):
    now_a, now_b = l[i + 1], r[i + 1]
    dp[i + 1][0] = min(dp[i][0] + abs(now_a - x) + abs(now_a - y))