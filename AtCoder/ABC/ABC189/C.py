n = int(input())
a = list(map(int,input().split()))
ans = 0
for i in range(n):
    mi = a[i]
    for j in range(i, n):
        mi = min(mi, a[j])
        ans = max(ans, mi * (j - i + 1))
print(ans)