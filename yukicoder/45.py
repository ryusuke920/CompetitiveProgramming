N = int(input())
V = list(map(int, input().split()))

if N <= 2:
    exit(print(max(V)))

dp = [0]*N
dp[0] = V[0]
dp[1] = max(dp[0], V[1])

for i in range(2, N):
    dp[i] = max(dp[i - 1], dp[i - 2] + V[i])

print(max(dp))