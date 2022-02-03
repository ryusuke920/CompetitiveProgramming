def CC(A: list) -> list:
    "座標圧縮"
    B = {j: i + 1 for i, j in enumerate(set(A))}
    return B
from bisect import bisect_left
n, q = map(int,input().split())
a = list(map(int,input().split()))
#num = CC(a)
l = [a[0] - 1]
for i in range(n - 1):
    l.append(a[i + 1] - a[i] - 1)
#print(l)
for i in range(n - 1):
    l[i + 1] += l[i]
#print(l)
for i in range(q):
    k = int(input())
    x = bisect_left(l, k)
    if x == len(l):
        #print("上")
        print(a[-1] + (k  - l[-1]))
    else:
        #print("した")
        print(a[x] + (k - l[x]) - 1)