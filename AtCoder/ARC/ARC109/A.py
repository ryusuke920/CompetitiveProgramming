a,b,x,y = map(int,input().split())
if a == b:
    print(x)
elif a > b:
    q1 = x*(a-b) + x*(a-b-1)
    q2 = y*(a-b - 1) + x
    print(min(q1,q2))
else:
    q1 = x*(b-a) + x*(b-a+1)
    q2 = y*(b-a)+x
    print(min(q1,q2))