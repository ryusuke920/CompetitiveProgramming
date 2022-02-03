x,y = map(int,input().split())
if x*4 < y or x*2 > y or y%2 == 1:
    print("No")
else:
    print("Yes")