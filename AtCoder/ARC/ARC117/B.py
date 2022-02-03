n = int(input())
a = list(map(int,input().split()))
mod = 10 ** 9 + 7
a = list(set(a))
a.sort()
x = []

for i in range(len(a) - 1):
    x.append(a[i + 1] - a[i] + 1)

ans = 1
for i in range(len(x)):
    ans *= x[i]
    ans %= mod

ans *= (a[0] + 1)
print(ans % mod)