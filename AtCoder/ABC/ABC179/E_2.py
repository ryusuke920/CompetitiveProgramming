n,x,m=map(int,input().split())
p=[0]*(m+1)
a=x
t=0
s=0
for i in range(2*m):
    if p[a]==1:
        p[a]=2
        break
    else:
        p[a]=1
        a=a**2%m
a=x
S=0
for i in range(2*m):
    if p[a]==1:
        s+=1
        S+=a
        a=a**2%m
    else:
        s+=1
        S+=a
        break
T=0
A=0
for i in range(2*m):
    a=a**2%m
    t+=1
    T+=a
    if p[a]==2:
        A=a
        break
a = x
if n <= s:
    ans=0
    for i in range(n):
        ans+=a
        a=a**2%m
    print(ans)
else:
    ans=S
    a=A
    n-=s
    ans+=(n//t)*T
    n=n%t
    for i in range(n):
        a=a**2%m
        ans+=a
    print(ans)