import sys
input = sys.stdin.readline

def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] += s[i] + a[i]
    # dp[i][j] := [i, j] までの区間のコストの最小値

    INF = 10**18
    dp = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][i] = 0
    
    for w in range(2, n + 1): # 幅(1 ~ N)
        for l in range(n - w + 1):
            # [l, r] に対する区間処理
            # [l, i - 1] + [i, r] で処理する
            r = l + w - 1
            for i in range(l, r):
                #print(w, l, r, i)
                dp[l][r] = min(dp[l][r], dp[l][i] + dp[i + 1][r] + (s[r + 1] - s[l]))

    #print(*dp,sep="\n")
    print(dp[0][n - 1])


if __name__ == "__main__":
    main()