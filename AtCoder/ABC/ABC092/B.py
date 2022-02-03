n = int(input())
d,x = map(int,input().split())
a = [int(input()) for i in range(n)]
ans = 0
count = 0
for i in range(n):
    if a[i] >= d:
        count += 1
    elif a[i] == 1:
        a[i] = d // a[i]
        ans += a[i]
    else:
        a[i] = (d-1) // a[i] + 1
        ans += a[i]
print(ans+x+count)