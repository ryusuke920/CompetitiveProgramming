n=int(input())
sp=[input().split() for i in range(n)]
sum=0
for i in range(n):
    sum+=int(sp[i][1])
ans=0
for i in range(n):
    if int(sp[i][1])>ans:
        ans=max(ans,int(sp[i][1]))
        ind=i
if ans > sum/2:
    print(sp[ind][0])
else:
    print("atcoder")