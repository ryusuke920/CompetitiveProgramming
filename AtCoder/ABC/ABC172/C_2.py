from bisect import bisect_left
n, m, k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
for i in range(n - 1):
    a[i + 1] += a[i]
for i in range(m - 1):
    b[i + 1] += b[i]
b = [0] + b
ans = 0
for i in range(n):
    x = i + 1
    t = bisect_left(b, a[i])
    if a[i] + b[t]:
        ans = max(ans, x + t)
if k >= b[0]:
    ans = max(ans, 1)
print(ans)