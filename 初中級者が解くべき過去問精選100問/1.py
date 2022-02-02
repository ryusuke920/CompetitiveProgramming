#2020/11/5
while True:
    n,x = map(int,input().split())
    ans = 0
    if (n,x) == (0,0):
        break
    for i in range(1,n-1):
        for j in range(i+1,n):
            for k in range(j+1,n+1):
                if i+j+k == x:
                    ans += 1
    print(ans)