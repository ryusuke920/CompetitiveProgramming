w,h,x,y,r = map(int,input().split())
if x-r >= 0 and x+r <= w and y-r >= 0 and y+r <= h:
    print("Yes")
else:
    print("No")