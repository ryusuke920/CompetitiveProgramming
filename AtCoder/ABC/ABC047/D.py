n, t = map(int, input().split())
a = list(map(int, input().split()))

mi = [0] * n
mi[0] = a[0]
for i in range(1, n):
    mi[i] = min(a[i], mi[i - 1])

max_num = 0
for i in range(n):
    max_num = max(max_num, a[i] - mi[i])

ans = 0
for i in range(n):
    if a[i] - mi[i] == max_num:
        ans += 1

print(ans)