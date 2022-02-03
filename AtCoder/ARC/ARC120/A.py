n = int(input())
a = list(map(int,input().split()))
ma = a[0]
ans = 0
wa = 0
r = [0] * (n + 1)
r[1] = a[0]
for i in range(n - 1):
    r[i + 2] += r[i + 1] + a[i + 1]

for i in range(n):
    ma = max(ma, a[i])
    wa += r[i + 1]
    ans = (i + 1) * ma + wa
    print(ans)