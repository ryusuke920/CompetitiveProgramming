from math import pi

c = int(input())
a, b = map(int, input().split())

print(pi * pi / 4 * (a + b) * (b - a) * (b - a) * c)