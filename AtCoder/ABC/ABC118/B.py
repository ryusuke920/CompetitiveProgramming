n,m = map(int,input().split())
ans = [0]*30
for i in range(n):
    a = list(map(int,input().split()))
    for j in range(a[0]+1):
        if j != 0:
            ans[a[j]-1] += 1
count = 0
for i in range(30):
    if ans[i] == n:
        count += 1
print(count)