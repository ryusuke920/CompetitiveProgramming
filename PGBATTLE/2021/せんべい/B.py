t = int(input())
mi = []
ma = []
for i in range(1, 10 ** 6):
    ma.append(i * (i - 1) // 2)

from bisect import bisect_left, bisect_right
from math import floor, ceil
for _ in range(t):
    n, m = map(int,input().split())
    if n - 1 <= m:
        ans_mi = 1
    else:
        ans_mi = n - m

    t = bisect_right(ma, m)
    num = n * (n - 1) // 2 - m
    b = -3 - 2 * n
    c = -2 * m + n + 2 + n ** 2
    ans_ma = ceil(-((b + (b ** 2 - 4 * c) ** 0.5) / 2))
    if m == 0:
        ans_ma = n
    print(ans_mi, ans_ma)