n = int(input())
a = list(map(int,input().split()))
ans = []
for i in range(n-2):
    ans.append(min(a[i],a[i+1]))
print(a[0],*ans,a[-1])