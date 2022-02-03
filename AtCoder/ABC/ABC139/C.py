N=int(input())
H=list(map(int,input().split()))
max=0
ans=0
for i in range(N-1):
    if H[i]>=H[i+1]:
        max+=1
    else:
        max=0
    if ans<=max:
        ans=max
print(ans)