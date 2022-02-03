n = int(input())
ans = 0
x = [input() for _ in range(n)]
flag = [False for i in range(9)]

for i in range(n):
    for j in range(9):
        if x[i][j] == "x":
            ans += 1
        elif x[i][j] == "o" and not flag[j]:
            ans += 1
            flag[j] = True
        if x[i][j] != "o":
            flag[j] = False
print(ans)