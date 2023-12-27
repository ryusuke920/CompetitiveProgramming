n = int(input())
s = [input() for _ in range(n)]

h, w = [0] * n, [0] * n

for i in range(n):
    cnt = 0
    for j in range(n):
        if s[i][j] == "o":
            cnt += 1
    h[i] = cnt

for i in range(n):
    cnt = 0
    for j in range(n):
        if s[j][i] == "o":
            cnt += 1
    w[i] = cnt

ans = 0
for i in range(n):
    for j in range(n):
        if s[i][j] == "o":
            ans += max(0, h[i] - 1) * max(0, w[j] - 1)

print(ans)