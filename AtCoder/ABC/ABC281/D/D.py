import sys
input = sys.stdin.readline

def main() -> None:
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    # dp[i][j][k] := i番目までで j 個選んだ時の d で割った余りが k となるような最大値
    dp = [[[-1] * D for _ in range(K + 1)] for _ in range(N + 1)]
    dp[0][0][0] = 0
    for i in range(1, N + 1):
        for j in range(K + 1):
            if j > i:
                continue
            for k in range(D):
                # 選ばない
                dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k])
                # 選ぶ
                if 0 <= j - 1 and dp[i - 1][j - 1][(k - A[i - 1]) % D] != -1:
                    dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - 1][(k - A[i - 1]) % D] + A[i - 1])

    print(dp[N][K][0])


if __name__ == "__main__":
    main()