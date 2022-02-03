while True:
    n, k = map(int,input().split())
    if (n, k) == (0, 0):
        exit()
    x = list(map(int,input().split()))
    x.sort()
    ans = 0
    for i in range(k):
        ans += x[i]
    print(ans)