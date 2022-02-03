n = int(input())
a = list(map(int,input().split()))
ans = 0
for i in range(n-1):
    ans += a[i+1] - a[i]
print(ans/(n-1))