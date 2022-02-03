n = int(input())
a = [int(input()) for _ in range(n)]
ans = num = 0
for i in range(n):
    if a[i] != 0:
        num += a[i]
    else:
        ans += num // 2
        num = 0
ans += num // 2
print(ans)