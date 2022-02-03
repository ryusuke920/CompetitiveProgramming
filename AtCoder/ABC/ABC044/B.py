w=input()
ans={}
k=0
for i in w:
    if i not in ans:
        ans[i]=1
    else :
        ans[i]+=1
for i in ans:
    if ans[i]%2==1:
        print("No")
        break
else :
    print("Yes")