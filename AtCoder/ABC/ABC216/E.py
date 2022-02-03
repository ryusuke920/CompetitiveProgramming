n, k = map(int,input().split())
a = list(map(int,input().split()))
a.sort(reverse=True)
wa = [0] * n
for i in range(n - 1):
    wa[i] = a[i] - a[i + 1]
a.append(0)

ans = 0
i = 0
cnt = 0
while True:
    if k <= 0 or i >= n:
        exit(print(ans))

    now_cnt = min(wa[i], k) # 今回やるべき数

    up = (a[i] * (a[i] + 1) // 2)
    under = (a[i + 1] * (a[i + 1] + 1) // 2)

    now_num = (up - under) * (i + 1)

    if k - (a[i] - a[i + 1]) * (i + 1) < 0:
        t = k // (i + 1)
        r = k % (i + 1)
        up = a[i] * (a[i] + 1) // 2
        under = (a[i] - t) * (a[i] - t + 1) // 2
        under = max(under, 0)
        ans += (up - under) * (i + 1) + r * (a[i] - t)
        k = 0
    else:
        ans += now_num

    k -= now_cnt * (i + 1)
    i += 1