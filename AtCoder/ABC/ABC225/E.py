from decimal import Decimal

n = int(input())
xy = []
for i in range(n):
    x, y = map(Decimal, input().split())
    if x - 1 == 0:
        xy.append(((y - 1) / x, 10 ** 18))
    else:
        xy.append(((y - 1) / x, y / (x - 1)))

xy.sort(key=lambda x: x[1])

ans = 0
now_r = 0
for l, r in xy:
    if now_r <= l:
        now_r = r
        ans += 1

print(ans)