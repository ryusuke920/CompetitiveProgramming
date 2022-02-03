a,b,x = map(int,input().split())
mi = a//x
ma = b//x
if (a%x == 0):
    print(ma-mi+1)
else:
    print(ma-mi)