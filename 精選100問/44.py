def DP(n: int) -> None:
    dp = [i for i in range(n + 1)]
    odd_dp = [i for i in range(n + 1)]

    # dp[i] := iを作るのに必要な最小の正四面体数の数
    for i in range(1, n + 1):

        p = i * (i + 1) * (i + 2) // 6
        
        if p > n:
            break

        for j in range(n - p + 1):
            dp[j + p] = min(dp[j + p], dp[j] + 1)

        if p % 2 == 1:
            for j in range(n - p + 1):
                odd_dp[j + p] = min(odd_dp[j + p], odd_dp[j] + 1)

    print(dp[n], odd_dp[n])

while True:
    n = int(input())
    if n == 0:
        exit()
    DP(n)