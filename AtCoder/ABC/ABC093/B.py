a,b,k = map(int,input().split())
ans = []
for i in range(a,a+k):
    if i <= b:
        ans.append(i)
if b-a+1 >= 2*k:
    for j in range(b-k+1,b+1):
        ans.append(j)
else:
    for j in range(a+k,b+1):
        if j <= b:
            ans.append(j)

for i in range(len(ans)):
    print(ans[i])