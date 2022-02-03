n,a,b = map(int,input().split())
if (b-a)%2:
    x = (a+b-1)//2
    print(min(x,n-x))
else:
    print((b-a)//2)