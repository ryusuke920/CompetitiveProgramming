#n = int(input())
x,y ,z = map(int,input().split())
#a = list(map(int,input().split()))
ans = cnt = 0
if x ** 2 + y ** 2 < z ** 2:
    print("Yes")
else:
    print("No")