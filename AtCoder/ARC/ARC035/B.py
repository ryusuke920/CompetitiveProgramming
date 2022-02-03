from collections import Counter
n = int(input())
t = [int(input()) for _ in range(n)]
cnt = num = 0
x = Counter(t)
x = x.most_common()
mod = 10 ** 9 + 7
t.sort()
for i in range(n):
    num += t[i]
    cnt += num

def fac(count): # 回数
    a = 1
    for i in range(2, count + 1):
        a *= i
        a %= mod
    return a

ans = 1
for i in range(len(x)):
    ans *= fac(x[i][1])
print(cnt)
print(ans % mod)