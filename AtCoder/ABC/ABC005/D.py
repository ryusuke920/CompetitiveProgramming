import sys
input = sys.stdin.readline
n = int(input())
d = [list(map(int,input().split())) for _ in range(n)]
q = int(input())
p = [int(input()) for _ in range(q)]

s = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(n):
    for j in range(n):
        s[i + 1][j + 1] = s[i][j + 1] + s[i + 1][j] - s[i][j] + d[i][j]

ans = [0] * (n ** 2 + 1)
for i in range(n):
    for j in range(i + 1, n + 1):
        for k in range(n):
            for l in range(k + 1, n + 1):
                num = s[j][l] - s[i][l] - s[j][k] + s[i][k]
                ans[(j - i) * (l - k)] = max(num, ans[(j - i) * (l - k)])

for i in range(n ** 2):
    ans[i + 1] = max(ans[i + 1], ans[i])

for i in range(q):
    print(ans[p[i]])