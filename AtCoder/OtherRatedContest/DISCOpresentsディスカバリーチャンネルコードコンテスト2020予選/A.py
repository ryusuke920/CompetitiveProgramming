x,y = map(int,input().split())
if x == 1 and y == 1:
    print(1000000)
elif x == 1 and y == 2 or x == 2 and y == 1:
    print(500000)
elif x == 2 and y == 2 or x == 3 and y == 1 or x == 1 and y == 3:
    print(400000)
elif x == 3 and y == 2 or x == 2 and y == 3 or x == 1 and y >= 4 or x >= 4 and y == 1:
    print(300000)
elif x == 3 and  y == 3 or x == 2 and y >= 4 or x >= 4 and y == 2:
    print(200000)
elif x == 3 and y >= 4 or x >= 4 and y == 3:
    print(100000)
else:
    print(0)