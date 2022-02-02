while True:
    w, h = map(int,input().split())
    if w == 0 and h == 0:
        exit()
    grid = [[10 ** 5] * w for _ in range(h)]
    for i in range(w + h - 1):
        a, b, c = map(int,input().split())
        a -= 1
        b -= 1
        grid[b][a] = c
    
    from collections import defaultdict
    dw = defaultdict(int)
    for i in range(h):
        for j in range(w - 1):
            if grid[i][j + 1] != 10 ** 5 and grid[i][j] != 10 ** 5:
                dw[f'{j + 1}_{j}'] += 1
    dh = defaultdict(int)
    for i in range(w):
        for j in range(h - 1):
            if grid[j + 1][i] != 10 ** 5 and grid[j][i] != 10 ** 5:
                dh[f'{j + 1}_{j}'] += 1
    ma = -1
    for i, j in dw.items():
        ma = max(ma, j)
    for i, j in dh.items():
        ma = max(ma, j)
    if len(dw) + len(dh) >= w + h - 3 and ma == 1:
        print("YES")
    else:
        print("NO")
    #print()