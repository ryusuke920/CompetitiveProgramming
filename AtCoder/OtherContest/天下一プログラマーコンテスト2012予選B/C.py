n = int(input())
t = []
for i in range(n):
    x, y = map(str,input().split())
    x = int(x[:2]) * 100 + int(x[3:])
    y = int(y[:2]) * 100 + int(y[3:])
    if x >= 2401:
        x -= 2400
    if y >= 2401:
        y -= 2400
    t.append([x, y])
print(*t,sep ="\n")
seki = [0] * (100 * 24 + 1)
ans = 1
for i in range(n):
    ch = 0
    if t[i][0] < t[i][1]:
        for j in range(t[i][0], t[i][1]):
            #print(j)
            if ch == 0 and seki[j] != 0:
                ch = 1
                ans += 1
            seki[j] += 1
    else:
        for j in range(t[i][0], 2400):
            if ch == 0 and seki[j] != 0:
                ch = 1
                ans += 1
            seki[j] += 1
        for j in range(0, t[i][1]):
            if ch == 0 and seki[j] != 0:
                ch = 1
                ans += 1
            seki[j] += 1
print(ans)