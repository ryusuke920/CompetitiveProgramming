n = int(input())
a = list(map(int, input().split()))

'''
平均 : a1, a2, ..., ap >= k
sum(a) / p >= k
sum(a) >= kp
sum(a) - kp >= 0
(a1 + a2 + ... + ap) - k * p >= 0
(a1 + a2 + ... + ap) - (k + k + k + ... + k) >= 0
(a1 - k) + (a2 - k) + (a3 - k) + ... + (ap - k) >= 0
'''

# dp[i] := i番目までで平均をK以上にできるかどうか <=> dp[i] >= 0

# 平均値
l, r = 0, 10 ** 9 + 1
while r - l > 10 ** -5:
    mid = (r + l) / 2
    dp = [0] * (n + 1)

    dp[1] = a[0] - mid
    
    for i in range(n - 1):
        dp[i + 2] = max(dp[i + 1], dp[i]) + a[i + 1] - mid
    
    # 平均をmid以上に出来る
    if dp[-1] >= 0 or dp[-2] >= 0:
        l = mid
    else:
        r = mid

print(l)

# 中央値

'''
n = 6
k = 3
1 2 2 3 5 6
-1, -1, -1, +1, +1, +1
'''

l, r = 0, 10 ** 9 + 1
while r - l > 1:
    mid = (r + l) // 2
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

    # 中央値をmid以上に出来る
    if dp[-1] >= 1 or dp[-2] >= 1:
        l = mid
    else:
        r = mid

print(l)