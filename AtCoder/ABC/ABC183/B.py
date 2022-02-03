
x1,y1,x2,y2 = map(int,input().split())
#a = list(map(int,input().split()))
ans = cnt = 0
d = abs(x2-x1)
ans = (y1*x2+y2*x1)/(y1+y2)
print(ans)