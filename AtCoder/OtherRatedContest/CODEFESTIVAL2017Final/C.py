from itertools import product
from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

d = defaultdict(int)
for i in range(n):
    d[a[i]] += 1

if d[0] >= 2 or d[12] >= 2:
    exit(print(0))

time = [0] * 11
for i in range(11):
    if d[i + 1] >= 3:
        exit(print(0))
    if d[i + 1] == 2:
        time[i] = 2
    elif d[i + 1] == 1:
        time[i] = 1

print(time)