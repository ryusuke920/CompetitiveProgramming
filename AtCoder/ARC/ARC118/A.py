from math import floor, ceil
t, n = map(int,input().split())

a = ceil((100 * n) / t)

print(floor((100 + t) * a / 100) - 1)