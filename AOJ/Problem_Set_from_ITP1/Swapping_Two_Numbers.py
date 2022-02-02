while True:
    x,y = map(int,input().split())
    if (x, y) == (0, 0):
        exit()
    print(min(x,y), max(x,y))