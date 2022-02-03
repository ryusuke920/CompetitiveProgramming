from collections import Counter
n = int(input())
s = input()
x = Counter(s)
x = x.most_common()
ans = 1
mod = 10 ** 9 + 7
for i in range(len(x)):
    ans *= (x[i][1] + 1)
    ans %= mod
print((ans - 1) % mod)