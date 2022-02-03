#n = int(input())
x, y = map(int,input().split())
#a = list(map(int,input().split()))
ans = cnt = 0
if x != y:
    print(3 - (x + y))
else:
    print(x)