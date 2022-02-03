x1,y1,x2,y2,x3,y3 = map(int,input().split())
x2 -= x1
x3 -= x1
y2 -= y1
y3 -= y1
print(abs(x2*y3-x3*y2)/2)