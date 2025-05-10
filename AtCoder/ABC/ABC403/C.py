N, M, Q = map(int, input().split())
from collections import defaultdict
d = defaultdict(list)
ok = [False]*(N + 1)
for i in range(Q):
    a = list(map(int, input().split()))
    if a[0] == 1:
        X, Y = a[1], a[2]
        d[f"{X}-{Y}"] = 1
    if a[0] == 2:
        X = a[1]
        d[X] = True
    if a[0] == 3:
        X, Y = a[1], a[2]
        if d[X]:
            print("Yes")
        else:
            if d[f"{X}-{Y}"] == 1:
                print("Yes")
            else:
                print("No")