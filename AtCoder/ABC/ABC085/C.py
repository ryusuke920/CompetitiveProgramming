n,y = map(int,input().split())
ans = [0]*3
for i in range(n+1):
    for j in range(n+1):
        if i*10000 + j*5000 + (n-i-j)*1000 == y and (n-i-j) >= 0:
            print(i,j,n-i-j)
            exit()
else:
    print(-1,-1,-1)