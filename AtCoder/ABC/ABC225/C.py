n, m = map(int,input().split())
b = [list(map(int,input().split())) for _ in range(n)]

bool = True

for i in range(n):
    for j in range(m - 1):
        if b[i][j + 1] - b[i][j] != 1:
            bool = False

for i in range(n - 1):
    for j in range(m):
        if b[i + 1][j] - b[i][j] != 7:
            bool = False


num = []
for i in range(m):
    if b[0][i] % 7:
        num.append(b[0][i] % 7)
    else:
        num.append(7)

for i in range(m - 1):
    if num[i] < num[i + 1] and num[i + 1] - num[i] == 1: continue
    bool = False

if bool:
    print('Yes')
else:
    print('No')