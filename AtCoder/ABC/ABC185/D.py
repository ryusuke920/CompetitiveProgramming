import math
n, m = map(int,input().split())
a = list(map(int,input().split()))
ans = ch = 0
if m == 0: exit(print(1))
a.sort()
cnt = max(1, a[0] - 1)
for i in range(m - 1):
    if a[i + 1] - a[i] - 1 != 0:
        ch = 1
    cnt = min(cnt, max(a[i + 1] - a[i] - 1, 1))
if ch == 0: exit(print(0))

ans = math.ceil((a[0] - 1) / cnt)
for i in range(m - 1):
    ans += math.ceil((a[i + 1] - a[i] - 1) / cnt)
ans += math.ceil((n - a[-1]) / cnt)
print(ans)