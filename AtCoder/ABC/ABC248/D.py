from collections import defaultdict
from bisect import bisect_left, bisect_right

n = int(input())
a = list(map(int, input().split()))

d = defaultdict(list)
for i in range(n):
    d[a[i]].append(i + 1)

for _ in range(int(input())):
    l, r, x = map(int, input().split())
    print(bisect_right(d[x], r) - bisect_left(d[x], l))