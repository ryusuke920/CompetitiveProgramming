a = list(map(int,input().split()))
k = int(input())
ans = 0
a.sort()
a[2] = a[2]*2**k
for i in range(3):
    ans += a[i]
print(ans)