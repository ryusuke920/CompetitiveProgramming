#    #..#.....#...##
from math import ceil
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
a = [0] + a + [n + 1]

if a[1] != 1:
    d = [a[1] - 1]
else:
    d = []

for i in range(m):
    if a[i + 2] - a[i + 1] - 1 != 0:
        d.append(a[i + 2] - a[i + 1] - 1)
if len(d) == 0:
    print(0)
else:
    k = min(d)
    ans = 0
    for i in d:
        ans += ceil(i / k)

    print(ans)