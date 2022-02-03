from collections import defaultdict
n, k = map(int, input().split())
a = list(map(int, input().split()))

s = [0]
for i in range(n):
    s.append(s[-1] + a[i])

d = defaultdict(int)
ans = 0
for r in s:
    ans += d[r - k]
    d[r] += 1

print(ans)