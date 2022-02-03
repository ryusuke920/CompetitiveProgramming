n = int(input())
a = list(map(int,input().split()))
for i in range(n):
    a[i] %= 200

num = [[] for _ in range(200)]

for i in range(n):
    cnt = a[i]
    cnt %= 200
    num[cnt].append([i + 1])

for i in range(n - 1):
    for j in range(i + 1, n):
        cnt = a[i] + a[j]
        cnt %= 200
        num[cnt].append([i + 1, j + 1])

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            cnt = a[i] + a[j] + a[k]
            cnt %= 200
            num[cnt].append([i + 1, j + 1, k + 1])

for i in range(len(num)):
    if len(num[i]) >= 2:
        print("Yes")
        print(len(num[i][0]), *num[i][0])
        print(len(num[i][1]), *num[i][1])
        exit()
print("No")