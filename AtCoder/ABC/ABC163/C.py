n = int(input())
a = list(map(int,input().split()))
ans = [0]*(n-1)
for i in range(n-1):
    ans[a[i]-1] += 1
for i in range(n-1):
    print(ans[i])
print(0)