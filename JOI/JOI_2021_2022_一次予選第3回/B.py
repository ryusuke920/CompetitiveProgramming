from math import ceil
s = int(input())
a = int(input())
b = int(input())
print(250 + ceil(max(0, s - a) / b) * 100)