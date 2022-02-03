from math import *
from decimal import *
x, y, r = map(Decimal,input().split())

ans = 0
for i in range(ceil(x - r), floor(x + r) + 1):
        num = (r ** 2 - (x - i) ** 2).sqrt()
        bottom = ceil(y - num)
        top = floor(y + num)
        ans += top - bottom + 1
print(ans)