n = int(input())
b = list(map(int,input().split()))
ans = []
for i in range(n):
    num = 0
    for j in range(len(b)):
        if j + 1 == b[j]:
            num = max(num, j + 1)
    if num == 0:
        exit(print(-1))
    ans.append(num)
    b = b[:num - 1] + b[num:]

print(*ans[::-1], sep = "\n")