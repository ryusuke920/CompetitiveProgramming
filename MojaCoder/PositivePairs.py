n = int(input())
a = list(map(int,input().split()))
x = a
x = x[::-1]
ans = 0
mod = 10 ** 9 + 7

num = [0] * n
num[0] = x[0]
for i in range(n - 1):
    num[i + 1] += x[i + 1] + num[i]

for i in range(n - 1):
    if a[i] > 0:
        ans += num[-i - 2] * a[i]
print(ans % mod)