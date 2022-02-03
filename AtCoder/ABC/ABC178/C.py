n = int(input())
mod = 10**9 + 7
ans = 1
for _ in range(n):
    ans *= 10
    ans %= mod

no1 = 1
no19 = 1
for _ in range(n):
    no1 *= 9
    no1 %= mod
for _ in range(n):
    no19 *= 8
    no19 %= mod
print((ans -(no1*2 - no19))%mod)