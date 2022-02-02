while True:
    n,m = map(int,input().split())
    if n == 0 and m == 0:
        break
    p = [list(map(int,input().split())) for _ in range(m)]
    ans = 0
    ch = 0
    for i in range(n):
        for j in range(m):
          ch += p[j][i]
        ans = max(ans,ch)
        ch = 0
    print(ans)