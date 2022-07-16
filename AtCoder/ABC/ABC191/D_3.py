from math import *

x, y, r = map(float, input().split())

ans = 0
for i in range(ceil(x - r), floor(x + r) + 1):
        num = sqrt((r ** 2 - (x - i) ** 2))
        bottom = ceil(y - num)
        top = floor(y + num)
        ans += top - bottom + 1
print(ans)