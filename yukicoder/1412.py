a, b, c, d = map(int, input().split())

if abs(a - c) + abs(b - d) <= 3 or a == c or b == d:
    print(1)
else:
    print(2)