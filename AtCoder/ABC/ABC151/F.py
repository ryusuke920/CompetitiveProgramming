from math import sqrt, hypot

def circumcenter(x1: float, y1: float, x2: float, y2: float, x3: float, y3: float):
    "三角形の外心を求める"
    a = x1
    b = y1
    c = x2
    d = y2
    e = x3
    f = y3

    aa = x1 * x1
    bb = y1 * y1
    cc = x2 * x2
    dd = y2 * y2
    ee = x3 * x3
    ff = y3 * y3

    if (2 * (e - a)*(b - d) - 2 * (c - a) * (b - f)) == 0: return None
    py = ((e - a) * (aa + bb - cc - dd) - (c - a) * (aa + bb - ee- ff)) / (2 * (e - a)*(b - d) - 2 * (c - a) * (b - f))

    px = (2 * (b - f) * py - aa - bb + ee + ff) / (2 * (e - a)) \
        if (c == a) else (2 * (b - d) * py - aa - bb + cc + dd) / (2 * (c - a))

    r = hypot(px - a, py - b)

    return px, py, r # (px, py, r) を中心とする円

n = int(input())

x, y = [0] * n, [0] * n
for i in range(n):
    x[i], y[i] = map(int,input().split())

if n == 2:
    exit(print(sqrt((x[0] - x[1]) ** 2 + (y[0] - y[1]) ** 2) / 2))

max_r = 0 # 直径の最大
for i in range(n - 1):
    for j in range(i + 1, n):
        d = sqrt((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2) / 2
        max_r = max(max_r, d)

#print(max_r)
r = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            dist = circumcenter(x[i], y[i], x[j], y[j], x[k], y[k])
            if dist != None:
                if dist[2] <= max_r + 10 ** -9:
                    r = max(r, dist[2])
#(5.0, 4.5, 6.726812023536856)
#6.726812023536856
#6.726812023536855
print(r)