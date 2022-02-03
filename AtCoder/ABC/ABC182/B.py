n = int(input())
a = list(map(int,input().split()))
ans = [0]*999
for i in range(2,1001):
    for j in range(n):
        if a[j]%i == 0:
            ans[i-2] += 1
print(ans.index(max(ans))+2)