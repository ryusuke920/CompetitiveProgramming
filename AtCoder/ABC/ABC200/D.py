from itertools import product
n = int(input())
a = list(map(int,input().split()))
n = min(n, 8)
a = a[:n]

num = [[] for _ in range(200)]
for i in product([0, 1], repeat = n):
    index = []
    cnt = 0
    for j in range(n):
        if i[j] == 1:
            index.append(j + 1)
            cnt += a[j]
    if len(index) >= 1:
        cnt %= 200
        num[cnt].append(index)
#print(*num,sep = "\n")
for i in range(len(num)):
    if len(num[i]) >= 2:
        print("Yes")
        print(len(num[i][0]), *num[i][0])
        print(len(num[i][1]), *num[i][1])
        exit()
print("No")