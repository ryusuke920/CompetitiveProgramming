n = int(input())
mod = 998244353
"""
x^2 - y = z^2
x^2 - z^2 = y
(x - z)(x + z) = y

p = x - z, q = x + z (q >= p)

1 <= pq = y <= n
1 <= x = (p + q) / 2 <= n

p <= q <= n/p

"""
ans = 0
for q in range(1, int(n ** 0.5) + 1):
    ans += (n // q - q) // 2 + 1
    ans %= mod

print(ans)