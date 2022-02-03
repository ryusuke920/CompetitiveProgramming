n = int(input())
a = list(map(int, input().split()))

# 平均値
l, r = 0, 10 ** 9 + 1
while r - l > 10 ** -4:
    mid = (l + r) / 2
    dp = [0] * (n + 1)
    dp[1] = a[0] - mid
    for i in range(n - 1):
        dp[i + 2] = max(dp[i + 1], dp[i]) + a[i + 1] - mid

    if dp[-1] >= 0 or dp[-2] >= 0:
        l = mid
    else:
        r = mid

print(l)

# 中央値
l, r = 0, 10 ** 9 + 1
while r - l > 1:
    mid = (l + r) // 2
    dp = [0] * (n + 1)
    
    if a[0] >= mid:
        dp[1] = 1
    else:
        dp[1] = -1
    
    for i in range(n - 1):
        if a[i + 1] >= mid:
            dp[i + 2] = max(dp[i + 1], dp[i]) + 1
        else:
            dp[i + 2] = max(dp[i + 1], dp[i]) - 1

    if dp[-1] >= 1 or dp[-2] >= 1:
        l = mid
    else:
        r = mid

print(l)