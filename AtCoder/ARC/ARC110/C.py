n = int(input())
p = list(map(int,input().split()))
ans = 0
now = 1
i = 0
num = []
cnt = 0
while True:
    for j in range(i, n):
        if p[j] == now:
            for k in reversed(range(i, j)):
                cnt += 1
                p[k], p[k + 1] = p[k + 1], p[k]
                num.append(k + 1)
            now = j + 1
            i = j
            break
    if now >= n - 1:
        break
    if cnt >= n:
        exit(print(-1))

ans = [i + 1 for i in range(n)]
if p == ans:
    print(*num, sep = "\n")
else:
    print(-1)