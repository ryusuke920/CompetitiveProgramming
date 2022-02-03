# 保留2020/12/2 21,22行目がわからぬ。
from bisect import bisect_left
n, q = map(int, input().split())
x = list(map(int,input().split()))
sx = [0]
for i in range(n):
    sx.append(sx[-1] + x[i])
#print(sx)
for i in range(q):
    num = 0
    c, d = map(int, input().split())
    # |Xi - c| <= d
    # -d <= |Xi - c| <= d
    # c - d <= Xi <= c + d (1)
    # c + d < Xi (2)
    # Xi < c - d (3)
    j1 = bisect_left(x, c - d) # (3)の場合
    j2 = bisect_left(x, c) # (1)の場合
    j3 = bisect_left(x, c + d) # (2)の場合
    num += d * j1 # c - d ジャストの人は該当しない (3)
    num += c * (j2 - j1) - sx[j2] + sx[j1]
    num += sx[j3] - sx[j2] - c * (j3 - j2)
    num += d * (n - j3) # (2)
    print(num)
print(j1,j2,j3)