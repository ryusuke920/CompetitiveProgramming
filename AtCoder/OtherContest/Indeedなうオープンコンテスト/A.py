a = int(input())
b = int(input())
mod = 10**9 + 7
ans = 0
if a >= b:
    a, b = b, a
for i in range(a,b+1):
    ans += i*i*(i+1)//2
    ans %= mod
print(ans%mod)