#n = int(input())
x, y = map(int,input().split())
#a = list(map(int,input().split()))
ans = cnt = 0
if x + y >= 15 and y >= 8:
    print(1)
elif x + y >= 10 and y >= 3:
    print(2)
elif x + y >= 3:
    print(3)
else:
    print(4)