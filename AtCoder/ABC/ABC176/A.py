x,y,z = map(int,input().split())
ans = 0
cnt = 0
if x%y == 0:
    print(x//y*z)
else:
    print(x//y*z+z)