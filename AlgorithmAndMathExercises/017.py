from math import gcd

n = int(input())
a = list(map(int, input().split()))

def lcm(a: int, b : int) -> int:
    '2数a, bのlcm(最小公倍数)を求める'
    g = gcd(a, b)
    return a * b // g

ans = lcm(a[0], a[1])
for i in range(n - 2):
    ans = lcm(ans, a[i + 2])

print(ans)