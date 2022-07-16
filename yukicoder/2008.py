n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

l = []
for i in range(n):
    l.append((a[i], b[i], (b[i] - 1) / a[i]))

l.sort(key=lambda x: x[2], reverse=True)
ans = 0
mod = 10 ** 9 + 7
level = 1
for i in range(n):
    ans += level * l[i][0]
    level *= l[i][1]
    level %= mod
    ans %= mod

print(ans)