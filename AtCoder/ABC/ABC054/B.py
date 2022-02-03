n,m = map(int,input().split())
a = [input() for _ in range(n)]
b = [input() for _ in range(m)]
for i in range(n-m+1):
    for j in range(n-m+1):
        cnt = 0
        for k in range(m):
            if a[i+k][j:j+m] == b[k]:
                cnt += 1
            if cnt == m:
                print("Yes")
                exit()
print("No")