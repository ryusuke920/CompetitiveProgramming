x,y = map(int,input().split())
ans = 4*x
if (y%2 == 0) and (ans >= y) and (2*x <= y):
    print("Yes")
else:
    print("No")