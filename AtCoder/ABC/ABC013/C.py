n, h = map(int, input().split())
a, b, c, d, e = map(int, input().split())

ans = 10 ** 20
for x in range(n + 1):
    y = max(0, ((n - x) * e - b * x - h) // (d + e) + 1)
    ans = min(ans, a * x + c * y)

print(ans)