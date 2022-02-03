#n = int(input())
x, y,z = map(int,input().split())
#a = list(map(int,input().split()))
ans = cnt = 0

if x != y and y != z and z != x:
    print(0)
elif x == y:
    print(z)
elif y == z:
    print(x)
else:
    print(y)