x1,y1,x2,y2=map(int,input().split())
X=x2-x1
Y=y2-y1
print(-(Y-x2),X+y2,-(Y-x1),X+y1)