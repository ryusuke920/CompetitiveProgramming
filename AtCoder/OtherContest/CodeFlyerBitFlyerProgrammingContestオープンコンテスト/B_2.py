from bisect import bisect_left, bisect_right
n, q = map(int,input().split())
x = list(map(int,input().split()))
x.sort()
wa = [x[0]]
for i in range(n - 1):
    wa.append(wa[-1] + x[i + 1])
wa = [0] + wa + [10 ** 18]
x = x + [10 ** 18]

"""
|Xi - c| <= d
-d <= Xi - c <= d
c - d <= Xi <= c + d & Xi >= c ... Xi - c 円(1)
c - d <= Xi <= c + d & Xi < c ... -(Xi - c) 円(2)
Xi < c - d ... d 円(3) <- 一番下
Xi > c + d ... d 円(4) <- 一番上
その他d円
"""
for i in range(q):
    ans = 0
    c, d = map(int,input().split())

    # (3)
    under = bisect_left(x, c - d)
    under_price = under * d
    ans += under_price

    # (4)
    top = bisect_left(x, c + d)
    top_price = (n - top) * d
    ans += top_price

    # (2)
    mid = bisect_left(x, c)
    mid_1_price = c * (mid - under) - (wa[mid] - wa[under])
    ans += mid_1_price

    # (1)
    mid_2_price = wa[top] - wa[mid] - c * (top - mid)
    ans += mid_2_price

    # print(under,mid,top)
    print(ans)