import sys
input = sys.stdin.readline
import math
n, h = map(int,input().split())
a, b = [0] * n, [0] * n
for i in range(n):
    a[i], b[i] = map(int,input().split())

right = []
ma = max(a)
for i in range(n):
    if ma < b[i]:
        right.append(b[i])
right.sort(reverse = True)

cnt = num = 0
for i in range(len(right)):
    cnt += 1
    num += right[i]
    if num >= h:
        exit(print(cnt))
print(math.ceil((h - num) / ma) + cnt)