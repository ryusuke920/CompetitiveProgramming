n,m,c = map(int,input().split())
b = list(map(int,input().split()))
count = 0
ans = 0
for i in range(n):
    a = list(map(int,input().split()))
    for j in range(m):
        ans += a[j]*b[j]
    if ans + c > 0:
        count += 1
        ans = 0
    else:
        ans = 0
print(count)