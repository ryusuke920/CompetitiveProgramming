n = int(input())
txy = [list(map(int,input().split())) for _ in range(n)]
t = txy[0][0]
go = txy[0][1] + txy[0][2]
if t < go or t%2 != go%2:
    print("No")
    exit()
for i in range(n-1):
    t = txy[i+1][0] - txy[i][0]
    go = abs(txy[i+1][1] - txy[i][1]) + abs(txy[i+1][2] - txy[i][2])
    if t < go or t%2 != go%2:
        print("No")
        exit()
print("Yes")