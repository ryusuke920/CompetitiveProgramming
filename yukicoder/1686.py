n = int(input())
a = list(map(int,input().split()))
ans = 0
for i in range(n):
    if a[i] - 1 not in a:
        ans += a[i]
print(ans)