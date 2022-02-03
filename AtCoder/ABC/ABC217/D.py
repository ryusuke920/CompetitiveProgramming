from bisect import bisect_right, insort
from array import array

l, q = map(int, input().split())
a = array('i', [0, l])

for _ in range(q):
    c, x = map(int, input().split())
    if c == 1:
        insort(a, x)
    elif c == 2:
        z = bisect_right(a, x)
        print(a[z] - a[z - 1])