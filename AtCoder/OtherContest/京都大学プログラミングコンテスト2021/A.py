n = int(input())
s = list(map(int,input().split()))
t = int(input())

from math import ceil
if max(s) % t == 0:
    print(max(s) // t)
else:
    print(ceil(max(s) / t))