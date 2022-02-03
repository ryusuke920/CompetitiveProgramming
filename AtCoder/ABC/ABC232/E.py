h, w, k = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())

dist = h + w - 2
if k == 1:
    if not (x1 == x2 or y1 == y2):
        exit(print(0))
    else:
        exit(print(1))
if k == 2:
    if x1 == x2 and y1 == y2:
        exit(print(dist))
    elif x1 == x2:
        exit(print(h - 2))
    elif y1 == y2:
        exit(print(w - 2))
    else:
        exit(print(2))

mod = 998244353
ans = dist
if k >= 4:
    ans += dist * 2

if k - 3 >= 0:
    ans += pow(dist * h * w, k - 3, mod)

if k >= 4:
    ans += dist + (h - 1) ** 2 + (w - 1) ** 2 + 2 * (h * w - (dist + 1))
ans %= mod
print(ans)