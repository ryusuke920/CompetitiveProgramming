n = int(input())
dp = [0]*(n+1)
mod = 10**9 +7
for i in range(3,n+1):
    tmp = 1
    for j in range(3,i-2):
        tmp += dp[j]
    dp[i] = tmp
print(dp[n]%mod)