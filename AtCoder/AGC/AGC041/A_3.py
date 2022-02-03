n,a,b = map(int,input().split())
x = a-1
y = n-b
if (b-a)%2 == 0:
    print((b-a)//2)
elif x<= y:
    print(x+1+(b-a-1)//2)
else:
    print(y+1+(b-a-1)//2)