a,b = map(int,input().split())
if a%16 == 0 and b%9 == 0:
    print("16:9")
else:
    print("4:3")