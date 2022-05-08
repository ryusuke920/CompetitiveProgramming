import sys
input = sys.stdin.readline

def main():
    n = int(input())
    x, y = map(int, input().split())

    INF = 10 ** 18
    # dp[i][j][k] := i番目までの弁当でたこ焼きを j, たい焼きを k, 買った時の弁当の個数の最小値
    dp = [[[INF] * 301 for _ in range(301)] for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0][0] = 0

    for i in range(n):
        a, b = map(int, input().split())
        for j in range(301):
            for k in range(301):
                dp[i + 1][j][k] = min(dp[i + 1][j][k], dp[i][max(0, j - a)][max(0, k - b)] + 1)
                # 買わない場合
                if dp[i + 1][j][k] > dp[i][j][k]:
                    dp[i + 1][j][k] = dp[i][j][k]

    ans = INF
    for i in range(x, 301):
        for j in range(y, 301):
            if ans > dp[n][i][j]:
                ans = dp[n][i][j]

    print(ans) if ans != INF else print(-1)

if __name__ == '__main__':
    main()