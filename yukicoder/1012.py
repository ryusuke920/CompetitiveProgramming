from bisect import bisect_left

n, q = map(int, input().split())
xw = [list(map(int, input().split())) for _ in range(n)]
x = list(map(int, input().split()))

xw.sort(key=lambda x: x[0])

sort_list = [xw[i][0] for i in range(n)]

accum_xw = [0]
accum_w = [0]
for i in range(n):
    accum_xw.append(accum_xw[-1] + xw[i][0] * xw[i][1])
    accum_w.append(accum_w[-1] + xw[i][1])

for i in range(q):
    t = bisect_left(sort_list, x[i])

    W = 2 * x[i] * accum_w[t]
    X = -2 * accum_xw[t]
    Y = accum_xw[-1]
    Z = -x[i] * accum_w[-1]
    ans = W + X + Y + Z
    print(ans, W, X, Y, Z, t)