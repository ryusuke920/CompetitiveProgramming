ans=''
s=input()
for i in s:
    if i=='B':
        ans=ans[:-1]
    else :
        ans+=i
print(ans)