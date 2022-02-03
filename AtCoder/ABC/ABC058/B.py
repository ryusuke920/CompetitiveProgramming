o=input()
e=input()
ans=''
for i in range(len(o)):
    ans+=o[i]
    if i<len(e):
        ans+=e[i]
print(ans)