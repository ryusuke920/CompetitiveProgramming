import bisect
n,m,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

for i in range(n-1):
    a[i+1] += a[i]
for j in range(m-1):
    b[j+1] += b[j]

ans = 0
cnt = m
for i in range(n):
    if cnt-1 >= 0:
        num = a[i] + b[cnt-1]
    while num > k:
        if cnt - 1 >= 0 and b[cnt-1] <= k:
            ans = max(ans, cnt)
        if cnt < 0:
            break
        cnt -= 1
        if cnt-1 >= 0:
            num = a[i] + b[cnt-1]
    if num <= k:
        ans = max(ans, (i+1)+cnt )
    if a[i] <= k:
        ans = max(ans, i+1)
    if cnt-1 >= 0 and b[cnt-1] <= k:
        ans = max(ans, cnt)
print(ans)