while True:
    h,w = map(int,input().split())
    if h == 0 and w == 0:
        break
    num = h**2 + w**2
    x = y = 0
    ans = 10**5
    for i in range(1,151):
        for j in range(1,151):
            cnt = i**2 + j**2
            if cnt < ans and cnt >= num:
                if cnt == num and i > h and j > i:
                    ans = cnt
                    x, y = i, j
                elif cnt > num and j > i:
                    ans = cnt
                    x, y = i, j
    print(x,y)