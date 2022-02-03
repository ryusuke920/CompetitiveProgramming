n, m, d = map(int,input().split())
if d == 0:
    print((m - 1) / n)
else:
    print((2 * (n - d)) / n ** 2 * (m - 1))