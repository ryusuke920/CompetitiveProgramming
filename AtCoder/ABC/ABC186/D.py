n = int(input())
a = list(map(int,input().split()))
a.sort()
ans = 0
for i in range(n - 1):
    ans += (a[i + 1] - a[i]) * (i + 1) * (n - i - 1)
print(ans)