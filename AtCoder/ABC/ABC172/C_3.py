from bisect import bisect_right

n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in range(m - 1):
    b[i + 1] += b[i]

ans = bisect_right(b, k)
cnt = 0
for i in range(n):
    cnt += a[i]
    if cnt > k:
        break
    t = bisect_right(b, k - cnt)
    ans = max(ans, i + 1 + t)

print(ans)