n=int(input())
ans=0
while True:
    ans+=n%10
    n//=10
    if n==0:
        break
print(ans)