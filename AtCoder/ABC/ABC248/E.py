from math import gcd
from collections import defaultdict

n, k = map(int, input().split())
xy = [list(map(int, input().split())) for _ in range(n)]

if k == 1:
    exit(print('Infinity'))

ans = set()
for i in range(n - 1):
    for j in range(i + 1, n):
        x1, y1, x2, y2 = xy[i][0], xy[i][1], xy[j][0], xy[j][1]
        # ax + by + c = 0 の (a, b, c) を求める
        a = y2 - y1
        b = x1 - x2
        c = x2 * y1 - x1 * y2
        cnt = 2
        for l in range(n):
            if i == l or j == l:
                continue
            x3, y3 = xy[l][0], xy[l][1]
            if a * x3 + b * y3 + c == 0:
                cnt += 1
        if cnt >= k:
            g = gcd(gcd(a, b), c)
            a //= g
            b //= g
            c //= g
            ans.add(max((a, b, c), (-a, -b, -c)))

print(len(ans))