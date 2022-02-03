n = int(input())
d = []
for i in range(n):
    s = input().split("/")
    M, D = int(s[0]), int(s[1])
    d.append([M, D])

d.sort(key=lambda x: x[0])
d.sort(key=lambda x: x[1])

num = [0] * 10 ** 3 # 休日か否か num[0] := 2012/1/1
num[0] = 1
for i in range(1, len(num)):
    if i % 7 == 6 or i % 7 == 0:
        num[i] = 1

date = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # 12月
for i in range(n):
    cnt = 0
    for j in range(d[i][0] - 1):
        cnt += date[j]
    cnt += d[i][1]
    if num[cnt - 1] == 0:
        num[cnt - 1] += 1
    else:
        t = 0
        while True:
            if num[cnt - 1 + t] == 0 or cnt - 1 + t >= 366:
                num[cnt - 1 + t] = 1
                break
            else:
                t += 1
ans = 0
ch = 0
s = 0
for i in range(366):
    if ch == 0:
        if num[i] == 1:
            ch = 1
            s = 1
    elif ch == 1:
        if num[i] == 1:
            s += 1
        else:
            ans = max(ans, s)
            s = 0
            ch = 0
print(max(ans, s))