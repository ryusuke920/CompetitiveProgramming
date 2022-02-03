n,x = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
ans = 0
if sum(a) == x:
    print(n)
    exit()
for i in range(n):
    x -= a[i]
    if x >= 0:
        ans += 1
    else:
        print(ans)
        exit()
print(n-1)