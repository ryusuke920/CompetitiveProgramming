n = int(input())
d = list(map(int,input().split()))
ans = 1
mod = 998244353
num = [0] * 10 ** 5
for i in range(n):
    num[d[i]] += 1

for i in range(max(d)):
    ans *= pow(num[i], num[i + 1], mod)

if d[0] != 0 or num[0] != 1:
    print(0)
else:
    print(ans % mod)