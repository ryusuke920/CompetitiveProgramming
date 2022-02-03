a, b = map(int,input().split())
num = []
numa = [1]
numb = [1]
if a == b and a != 1:
    cnt = 0
    for i in range(2, int(a ** 0.5) + 1):
        if a%i == 0:
            cnt = 1
    if cnt == 0:
        exit(print(2))

for i in range(2, int(a ** 0.5) + 1):
    if a%i == 0:
        numa.append(i)
        if a // i != i:
            numa.append(a // i)

for i in range(2, int(b ** 0.5) + 1):
    if b%i == 0:
        numb.append(i)
        if b // i != i:
            numb.append(b // i)

num = set(numa) & set(numb)
num = list(num)
num.sort()

ans = 0
for i in range(len(num)):
    cnt = 0
    for j in range(2, int(num[i] ** 0.5) + 1):
        if num[i]%j == 0:
            cnt = 1
            break
    if cnt == 0:
        ans += 1
print(ans)