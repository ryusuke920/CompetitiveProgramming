import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def main() -> None:
    mod = 998244353
    n, m, k = map(int, input().split())

    
    # dp[i][j] := i番目がjであるような通り数
    # dp[i + 1][j] = (dp[i][j - k] + dp[i][j - k - 1] + ... + dp[i][1])
    #              + (dp[i][j + k] + dp[i][j + k + 1] + ... + dp[i][m])
    # <=>
    # dp[i + 1][j] = accumlate_sum[j - k] + (accumulate_sum[m] - accumulate_sum[j + k - 1])

    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, m + 1):
        dp[1][i] = 1
    
    for i in range(1, n):

        accumulate_sum = [0] * (m + 1)
        for j in range(m):
            accumulate_sum[j + 1] = accumulate_sum[j] + dp[i][j + 1]
        
        for j in range(1, m + 1):
            
            if j - k >= 0:
                dp[i + 1][j] += accumulate_sum[j - k]
            
            if m > j + k - 1 and j + k - 1 > 0:
                dp[i + 1][j] += accumulate_sum[m] - accumulate_sum[j + k - 1]
            
            dp[i + 1][j] %= mod

    print(sum(dp[n][1 : m + 1]) % mod)


if __name__ == '__main__':
    main()