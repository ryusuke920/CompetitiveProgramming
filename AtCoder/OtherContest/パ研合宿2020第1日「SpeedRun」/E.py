x, y = map(int,input().split())
if x < y:
    print(x + 2 * y, y)
elif x > y:
    print(x, 2 * x + y)
elif (x, y) == (0, 0):
    print(114514, 114514)
else:
    print(-1)