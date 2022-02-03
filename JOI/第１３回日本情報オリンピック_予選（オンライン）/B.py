n,m = map(int,input().split())
a = [int(input()) for _ in range(n)]
b = [int(input()) for _ in range(m)]
ans = [0]*n
for i in range(m):
    mi = n
    for j in range(n):
        if a[j] <= b[i]:
            mi = min(mi, a[j])
            ind = j
    ans[ind] += 1
print(ans)