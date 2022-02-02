from math import gcd

n, m = map(int, input().split())
a = list(map(int ,input().split()))

num = a[0] // 2
for i in range(n):
    x = a[i] // 2
    g = gcd(num, x)
    if (num // g) % 2 != (x // g) % 2:
        exit(print(0))
    
    num = num * x // g

print((m // num + 1) // 2)