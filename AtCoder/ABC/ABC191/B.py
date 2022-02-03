n,x = map(int,input().split())
ans = []
a = list(map(int,input().split()))
for i in range(n):
    if a[i] != x:
        ans.append(a[i])
print(*ans)