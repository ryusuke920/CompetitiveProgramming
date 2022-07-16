from math import gcd


def s(x1: int, y1: int, x2: int, y2: int) -> int:
    return x1 * y2 - x2 * y1


n = int(input())
g = []
for _ in range(n):
    a, b = map(int, input().split())
    if b < 0:
        a *= -1
        b *= -1
    
    g.append((a, b))

for v1, v2 in g:
    
mod = 10 ** 9 + 7
