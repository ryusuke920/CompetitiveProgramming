from math import cos, radians

a, b, h, m = map(int, input().split())
x = h * 30 + m / 2
y = m * 6

deg = min(360 - abs(x - y), abs(x - y))
theta = cos(radians(deg))

ans = a ** 2 + b ** 2 - 2 * a * b * theta
print(ans ** 0.5)