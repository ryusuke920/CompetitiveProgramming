from math import ceil

x, y = map(int, input().split())
if x >= y:
    print(0)
else:
    print(ceil((y-x)/10))