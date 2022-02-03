n, now = map(int,input().split())
a = list(map(int,input().split()))
now -= 1
for i in range(n):
    a[i] -= 1

flag = [False] * n
flag[now] = True
while True:
    if not flag[a[now]]:
        flag[a[now]] = True
        now = a[now]
    else:
        break

print(flag.count(1))