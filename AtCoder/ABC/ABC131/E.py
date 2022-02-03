n, k = map(int,input().split())
ans = []
ma = (n - 1) * (n - 2) // 2

if k > ma:
    exit(print(-1))


for i in range(n - 1):
    ans.append((0, i + 1))

for i in range(n - 1):
    for j in range(i + 1, n):
        if k == ma:
            break
        ans.append((i + 1, j + 1))
        ma -= 1

print(len(ans))
for i, j in ans:
    print(i + 1, j + 1)