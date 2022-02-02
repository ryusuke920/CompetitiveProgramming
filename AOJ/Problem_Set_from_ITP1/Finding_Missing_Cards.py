n = int(input())
num = [[0]*13 for _ in range(4)]
for i in range(n):
    s,t = map(str,input().split())
    t = int(t)
    if s == "S":
        num[0][t - 1] = 1
    elif s == "H":
        num[1][t - 1] = 1
    elif s == "C":
        num[2][t - 1] = 1
    else:
        num[3][t - 1] = 1

ans = []
for i in range(4):
    for j in range(13):
        if num[i][j] == 0:
            if i == 0:
                ans.append(["S", j + 1])
            elif i == 1:
                ans.append(["H", j + 1])
            elif i == 2:
                ans.append(["C", j + 1])
            else:
                ans.append(["D", j + 1])

for i in range(len(ans)):
    print(*ans[i])