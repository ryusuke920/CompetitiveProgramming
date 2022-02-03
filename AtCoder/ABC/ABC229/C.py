n, w = map(int,input().split())
a = []
for i in range(n):
    x, y = map(int,input().split())
    a.append((x, y))
a.sort(reverse=True, key=lambda x: x[0])

now = 0
ans = 0
for i in range(n):
    if now >= w:
        break
    if now + a[i][1] <= w:
        now += a[i][1]
        ans += a[i][0] * a[i][1]
    else:
        ok = w - now
        ans += a[i][0] * ok
        now = w

print(ans)