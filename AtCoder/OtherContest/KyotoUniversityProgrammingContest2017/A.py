n, k = map(int,input().split())
a = list(map(int,input().split()))
a.sort(reverse = True)
ans = 0
for i in range(n):
    ans += a[i]
    if ans >= k:
        exit(print(i + 1))
print(-1)