n = int(input())
a = [[0, 0] for _ in range(n)]
ans = 0
for i in range(n):
    a[i][0], a[i][1] = int(input()), i + 1
a.sort()

for i in range(n):
    if a[i][1] % 2 != (i + 1) % 2:
        ans += 1
print(ans // 2)