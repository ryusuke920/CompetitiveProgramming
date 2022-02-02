while True:
    h,w = map(int,input().split())
    if (h,w) == (0,0):
        exit()
    for i in range(h):
        ans = ""
        for j in range(w):
            if i%2 == 0:
                if (j%2 == 0):
                    ans += "#"
                else:
                    ans += "."
            else:
                if (j%2 == 0):
                    ans += "."
                else:
                    ans += "#"
        print(ans)
    print()