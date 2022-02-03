t = input()
ans = cnt = i = 0
x = t
x = list(x)
for i in range(len(x)):
    if x[i] == "?" and i % 2 == 0:
        x[i] = "2"
    elif x[i] == "?" and i % 2 == 1:
        x[i] = "5"

for i in range(len(x)):
    if cnt == 0 and x[i] == "2" and i % 2 == 1:
        cnt += 1
    elif cnt >= 1 and (x[i] == "2" or x[i] == "5"):
        cnt += 1
    else:
        ans = max(ans, cnt // 2 * 2)
        cnt = 0
ans = max(ans, cnt // 2 * 2)
cnt = 0
for i in range(len(x)):
    if cnt == 0 and x[i] == "2" and i % 2 == 0:
        cnt += 1
    elif cnt >= 1 and (x[i] == "2" or x[i] == "5"):
        cnt += 1
    else:
        ans = max(ans, cnt // 2 * 2)
        cnt = 0
ans = max(ans, cnt // 2 * 2)
cnt = 0

x = t
x = list(x)
for i in range(len(x)):
    if x[i] == "?" and i % 2 == 1:
        x[i] = "2"
    elif x[i] == "?" and i % 2 == 0:
        x[i] = "5"

for i in range(len(x)):
    if cnt == 0 and x[i] == "2" and i % 2 == 0:
        cnt += 1
    elif cnt >= 1 and (x[i] == "2" or x[i] == "5"):
        cnt += 1
    else:
        ans = max(ans, cnt // 2 * 2)
        cnt = 0
ans = max(ans, cnt // 2 * 2)
cnt = 0
for i in range(len(x)):
    if cnt == 0 and x[i] == "2" and i % 2 == 1:
        cnt += 1
    elif cnt >= 1 and (x[i] == "2" or x[i] == "5"):
        cnt += 1
    else:
        ans = max(ans, cnt // 2 * 2)
        cnt = 0
ans = max(ans, cnt // 2 * 2)
print(ans)