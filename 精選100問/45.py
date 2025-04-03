n, m = map(int,input().split())
c = [int(input()) for _ in range(m)]
x = [int(input()) for _ in range(n)]

INF = 10 ** 18
# dp[i] := i番目までの２乗和が最小となる値
dp = [INF] * (n + 1)
dp[0] = 0

for i in range(n):
    