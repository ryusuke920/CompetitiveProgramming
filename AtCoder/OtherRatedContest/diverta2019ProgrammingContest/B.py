r,g,b,n = map(int,input().split())
cnt = 0
for i in range(0,n+1,r):
    for j in range(0,n+1-i,g):
        if (n - i - j)%b == 0 and (n - i - j)%b >= 0:
            cnt += 1
print(cnt)