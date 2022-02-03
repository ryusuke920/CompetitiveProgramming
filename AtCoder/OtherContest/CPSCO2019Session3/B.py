n,m = map(int,input().split())
a = list(map(int,input().split()))
a.sort(reverse = True)
i = 0
ans = 0
while ans < m:
    ans += a[i]
    i += 1
print(i)