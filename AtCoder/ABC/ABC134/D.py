n = int(input())
a = list(map(int,input().split()))
b = [False] * n

for i in range(1, n + 1):
    cnt = 0
    for j in range(n // i):
        if b[j] == True:
            cnt += 1
    if cnt % 2 != a[i - 1]:
        b[i] = True
ans = [i + 1 for i in b if b]
print(len(ans))
print(*ans)