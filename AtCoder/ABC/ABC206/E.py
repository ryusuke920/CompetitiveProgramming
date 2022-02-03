def extgcd(a: int, b: int) -> int:
    "ax + by = gcd(a,b) = d となる (x, y, d) を返す"
    if b == 0:
        return (1, 0, a)

    q, r = a // b, a % b
    x, y, d = extgcd(b, r)
    s, t = y, x - q * y

    return s, t, d # (qb + r)s + bt = dとなる s, t, d
from bisect import bisect_left
def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]: continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]


l, r = map(int,input().split())
#num = primes(100)

ans = 0
for i in range(l, r + 1):
    for j in range(r // i):
        x = extgcd(i, j)
        ans += x[0] * x[2] + x[1] - x[2]
        print(x)
print(ans)