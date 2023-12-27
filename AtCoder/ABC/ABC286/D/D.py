import sys
input = sys.stdin.readline

def main() -> None:
    n, x = map(int, input().split())
    
    a, b = [0] * n, [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    
    # dp[i][j] := i 番目までの硬貨で j 円を払うことができるか
    t = min(x, 100 * 50 * 50)
    dp = [[False] * (t + 10) for _ in range(n + 1)]
    dp[0][0] = True
    for i in range(n):
        for j in range(t + 1):
            for k in range(b[i] + 1): # 使う枚数
                if j - k * a[i] >= 0:
                    dp[i + 1][j] |= dp[i][j - k * a[i]]


    if dp[n][x]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()