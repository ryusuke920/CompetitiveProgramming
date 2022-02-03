l,r,d = map(int,input().split())
mi = l//d
ma = r//d
if l%d == 0:
    print(ma-mi+1)
else:
    print(ma-mi)