n = int(input())

for i in range(1, 10000):
    if n == i * (i - 1) // 2:
        cnt = i
        break
else:
    exit(print('No'))

print('Yes')
print(cnt)
ans = [[] for _ in range(cnt)]
num = 1
for i in range(cnt - 1):
    for j in range(i + 1, cnt):
        ans[i].append(num)
        ans[j].append(num)
        num += 1

for i in range(len(ans)):
    print(len(ans[i]), *ans[i])