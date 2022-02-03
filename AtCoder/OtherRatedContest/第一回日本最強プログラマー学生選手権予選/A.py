m,d = map(int,input().split())
cnt = 0
if d <= 19:
    print(0)
    exit()
for i in range(1,m+1):
    for j in range(20,d+1):
        if (j%10)*(j//10) == i and j%10 != 1:
            #print(i,j)
            cnt += 1
print(cnt)