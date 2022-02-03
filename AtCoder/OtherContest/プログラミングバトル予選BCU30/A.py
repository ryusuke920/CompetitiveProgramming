n = int(input())
a = list(map(int,input().split()))
ans = [0]*30
for i in range(n):
    ans[a[i]] += 1
print(*ans)