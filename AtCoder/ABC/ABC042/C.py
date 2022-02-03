n, k = map(int,input().split())
d = list(map(int,input().split()))
num = []
for i in range(10):
    if i != 0 and i not in d:
        num.append(i)

ok = []
for i in range(10):
    if i not in d:
        ok.append(i)

i = 0
while True:
    x = str(num[i])
    for j in range(len(ok)):
        t = x + str(ok[j])
        num.append(int(t))

    if len(str(num[-1])) >= 6:
        break
    i += 1
    if i >= 100000:
        break

for i in range(len(num)):
    if num[i] >= n:
        exit(print(num[i]))