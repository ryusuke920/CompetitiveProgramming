n = int(input())
a = list(map(int,input().split()))
ans = 0
cnt = a[0]
for i in range(1,n):
    ans += max(cnt-a[i],0)
    cnt = max(cnt,a[i])
print(ans)