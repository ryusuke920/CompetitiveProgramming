N, W=map(int,input().split())
WV = [list(map(int,input().split())) for i in range(N)]

lst = []
for v, w in WV:
    for i in range(len(lst)):
        w1,v1=lst[i]
        if w1:
            lst.append([w1 + w, v1 + v])
    lst.append([w, v])

    lst = sorted(lst, key=lambda x: x[0], reverse=True)
    while lst and lst[-1][0] == 0:
        lst.pop()

    w, v = lst[-1]
    for i in range(len(lst) - 1)[::-1]:
        w1,v1=lst[i]
        if v1<=v:
            lst[i][0]=0
            lst[i][1]=0
        else:
            v = v1

print(max([v for w, v in lst if w <= W]))