while True:
    a = list(map(int,input().split()))
    if a == [0, 0, 0, 0]:
        exit()

    while True:
        cnt = 0
        for i in a:
            if i == 0:
                cnt += 1
        if cnt >= 3:
            break

        mi = 10 ** 18
        for i in a:
            if i != 0:
                mi = min(mi, i)
        for i, j in enumerate(a):
            if j == mi:
                t = i
                break
        t = a.index(mi)

        for i in range(4):
            if i != t:
                a[i] -= mi
                a[i] = max(a[i], 0)

    for i in a:
        if i != 0:
            print(i)
            break