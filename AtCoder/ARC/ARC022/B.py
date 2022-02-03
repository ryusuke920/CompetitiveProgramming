from collections import defaultdict

n = int(input())
a = list(map(int,input().split()))

d = defaultdict(int)
l = 0
ans = 0
for r in range(n):
    d[a[r]] += 1
    if d[a[r]] == 2:
        while True:
            d[a[l]] -= 1
            l += 1
            if d[a[r]] == 1: break
    ans = max(ans, r - l + 1)

print(ans)