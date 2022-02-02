from math import gcd

n, x, y = map(int, input().split())
print(n // x + n // y - n // (x * y // gcd(x, y)))