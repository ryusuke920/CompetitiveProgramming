while True:
    x,y = map(int,input().split())
    if (x,y) == (0,0):
        exit()
    for i in range(x):
        print("#"*y)
    print()