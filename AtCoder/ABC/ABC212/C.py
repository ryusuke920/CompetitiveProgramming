n, m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
ans = cnt = 0
a.sort()
b.sort()
from bisect import bisect_left
ans = 10 ** 18

for i in range(n):
    t = bisect_left(b, a[i])
    if t == m:
        ans = min(ans, abs(b[t - 1] - a[i]))
    else:
        ans = min(ans, abs(b[t] - a[i]), abs(b[t - 1] - a[i]))

print(ans)