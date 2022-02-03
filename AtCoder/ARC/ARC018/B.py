from itertools import combinations
n = int(input())
x, y = [0] * n, [0] * n
for i in range(n):
    x[i], y[i] = map(int,input().split())

ans = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            x1, y1, x2, y2, x3, y3 = x[i], y[i], x[j], y[j], x[k], y[k]
            x1, y1, x2, y2 = (x1 - x3), (y1 - y3), (x2 - x3), (y2 - y3)
            # (x3, y3)分だけ並行移動させる
            r = abs(x1 * y2 - x2 * y1)
            if r != 0 and r % 2 == 0:
                ans += 1
print(ans)