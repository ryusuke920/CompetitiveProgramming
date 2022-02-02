while True:
    x,y = map(int,input().split())
    if (x,y) == (0,0):
        exit()
    print("#"*y)
    for i in range(x-2):
        ans = ""
        for j in range(y):
            if j == 0 or j == y - 1:
                ans += "#"
            else:
                ans += "."
        print(ans)
    print("#"*y)
    print()