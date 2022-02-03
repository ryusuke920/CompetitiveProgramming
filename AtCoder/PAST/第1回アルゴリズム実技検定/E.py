n, q = map(int,input().split())
num = [[0] * n for _ in range(n)]
for i in range(q):
    s = list(map(int,input().split()))
    if s[0] == 1:
        num[s[1] - 1][s[2] - 1] = 1
    elif s[0] == 2:
        cnt = [0] * n
        for j in range(n):
            if num[j][s[1] - 1] == 1:
                cnt[j] = 1
        for j in range(n):
            if cnt[j] == 1:
                num[s[1] - 1][j] = 1
    else: # s[0] == 3:
        cnt = [0] * n
        for j in range(n):
            if num[s[1] - 1][j] == 1:
                for k in range(n):
                    if num[j][k] == 1:
                        cnt[k] = 1
        for j in range(n):
            if cnt[j] == 1:
                num[s[1] - 1][j] = 1

for i in range(n):
    ans = ""
    for j in range(n):
        if i == j:
            ans += "N"
        elif num[i][j] == 1:
            ans += "Y"
        else:
            ans += "N"
    print(ans)   