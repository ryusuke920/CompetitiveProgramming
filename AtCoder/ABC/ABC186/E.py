t = int(input())

# ax + by = gcd(a, b), by ≡ 0 (mod n)?
def extgcd(a, b):
    if b == 0:
        return (1, 0, a)
    (x, y, g) = extgcd(b, a % b)
    return (y, x - a // b * y, g)

for i in range(t):
    n, s, k = map(int,input().split())
    (x, y, g) = extgcd(k, n)
    if s % g != 0:
        print(-1)
        continue
    s //= g
    n //= g
    k //= g
    print(((-s * x) % n + n) % n)