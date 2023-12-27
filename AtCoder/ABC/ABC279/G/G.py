import sys
input = sys.stdin.readline

def main() -> None:
    N, K, C = map(int, input().split())
    mod = 998244353
    dp = [0] * N
    dp[0] = C % mod
    for i in range(1, N):
        dp[i] += 2 * dp[i - 1] + (C - 2) * dp[max(0, i - (K - 1))]
        dp[i] %= mod
    print(dp[N - 1])


if __name__ == "__main__":
    main()