n,m = map(int,input().split())
ans = 0
for _ in range(n):
    count = 0
    a = list(map(int,input().split()))
    for j in range(m):
        if a[j] == 1:
            count += 1
    ans = max(ans,count)
print(ans)