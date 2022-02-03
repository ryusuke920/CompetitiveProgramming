n,k = map(int,input().split())
ans = [0]*n
for i in range(k):
    d = int(input())
    a = list(map(int,input().split()))
    for j in range(len(a)):
        ans[a[j]-1] += 1
print(ans.count(0))