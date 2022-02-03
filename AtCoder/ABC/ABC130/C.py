w,h,x,y = map(int,input().split())
if 2*x == w and 2*y == h:
    print(w*h//2,1)
else:
    print(w*h/2,0)