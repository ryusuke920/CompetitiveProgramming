n = int(input())
s = input()

mod = 998244353
a = [0] * 4
for i in s:
    if i == 'A':
        a[0] += 1
    if i == 'B':
        a[1] += 1
    if i == 'C':
        a[2] += 1
    if i == 'D':
        a[3] += 1

up = 1
for i in range(1, sum(a) + 1):
    up *= i
    up %= mod

b = [1] * 4
for i in range(4):
    for j in range(1, a[i] + 1):
        b[i] *= j
        b[i] %= mod

ans = up * pow(b[0], -1, mod)
ans %= mod
ans *= pow(b[1], -1, mod)
ans %= mod
ans *= pow(b[2], -1, mod)
ans %= mod
ans *= pow(b[3], -1, mod)
ans %= mod

x = 1
for i in range(1, a[0] + a[1] + 1):
    x *= i
    x %= mod
x *= pow(b[0], -1, mod)
x %= mod
x *= pow(b[1], -1, mod)
x %= mod

y = 1
for i in range(1, a[2] + a[3] + 1):
    y *= i
    y %= mod
y *= pow(b[2], -1, mod)
y %= mod
y *= pow(b[3], -1, mod)
y %= mod

print((ans - x * y + 1) % mod)