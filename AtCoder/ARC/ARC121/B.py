import sys
input = sys.stdin.readline
from bisect import bisect_left

n = int(input())
r, g, b = [], [], []
for i in range(2 * n):
    a, c = map(str,input().split())
    if c == "R":
        r.append(int(a))
    elif c == "G":
        g.append(int(a))
    else:
        b.append(int(a))

if (len(r) % 2 == 0) and (len(g) % 2 == 0) and (len(b) % 2 == 0):
    exit(print(0))

# zの配列が偶数個の配列になるようにする
if len(r) % 2 == 0: # Rが偶数個
    x, y, z = g, b, r
elif len(g) % 2 == 0: # Gが偶数個
    x, y, z = b, r, g
elif len(b) % 2 == 0: # Bが偶数個
    x, y, z = r, g, b

# 3つ奇数はありえない
x.sort()
y.sort()
z.sort()
INF = 10 ** 18
x = x + [INF]
y = y + [INF]
z = z + [INF]

ans = []
# (x, y)の１ペアで比較
for i in range(len(x) - 1):
    s = bisect_left(y, x[i])
    cnt = min(abs(y[s - 1] - x[i]), abs(y[s] - x[i]))
    ans.append(cnt)

# (x, z), (y, z)の２ペアでの比較
cnt_1, cnt_2 = [], []
for i in range(len(z) - 1):
    s = bisect_left(x, z[i])
    t = bisect_left(y, z[i])
    cnt_1.append(min(abs(x[s - 1] - z[i]), abs(x[s] - z[i])))
    cnt_2.append(min(abs(y[t - 1] - z[i]), abs(y[t] - z[i])))

if len(z) >= 2:
    ans.append(min(cnt_1) + min(cnt_2))

print(min(ans))