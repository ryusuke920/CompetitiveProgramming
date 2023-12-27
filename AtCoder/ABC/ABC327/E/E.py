def main():
    n = int(input())
    a = list(map(int, input().split()))
    dp = [[-999999999999.0 for _ in range(6060)] for _ in range(6060)]
    
    bunbo = [0] * 6060
    bunbo[1] = 1.0
    
    for i in range(2, 6060):
        bunbo[i] = bunbo[i - 1] * 0.9 + 1.0
    
    for i in range(n):
        dp[i + 1][1] = max(a[i], dp[i][1])
        
        for j in range(1, 6060):
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            
            if j - 1 > 0:
                nx = (dp[i][j - 1] * bunbo[j - 1]) * 0.9 + a[i]
                nx /= bunbo[j]
                dp[i + 1][j] = max(dp[i + 1][j], nx)
    
    ans = -999999999999
    
    for i in range(1, n + 1):
        ans = max(ans, dp[n][i] - 1200 / (i ** 0.5))
    
    print(ans)

if __name__ == "__main__":
    main()
