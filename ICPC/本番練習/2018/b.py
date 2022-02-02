while True:
    n,m,t,p = map(int,input().split())
    if n == 0 and m == 0 and t == 0 and p == 0:
        break
    squ = [[1 for i in range(n)]]*m
    left = 0
    under = m
    for i in range(t):
        d,c = map(int,input().split())
        if d == 1:
            left -= n
            left = min(left,n)
            for i in range(c):
                for j in range(under):
                    squ[i+c][j] += squ[i][j]
            squ = [0:][:3]
        else:
            under -= c
            under = max(under,0)
            for i in range(c):
                for j in range(left):
                    squ[i+under-2*c][j] += squ[i+under-c][j]
    ans = 0
    for i in range(p):
        x,y = map(int,input().split())
        ans += squ[left][under]
    print(ans)
    for i in range(m):
        print(squ[i])