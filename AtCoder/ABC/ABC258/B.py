n = int(input())
a = [list(map(int, input())) for _ in range(n)]

ma = -1
for i in a:
    for j in i:
        ma = max(ma, j)

p = set()
for i in range(n):
    for j in range(n):
        if a[i][j] == ma:
            p.add((i, j))

ans = 0
for i, j in p:
    for ii in range(-1, 2):
        for jj in range(-1, 2):
            if ii == 0 and jj == 0:
                continue

            num = ''
            for k in range(n):
                num += str(a[(i + k * ii) % n][(j + k * jj) % n])

                
                ans = max(ans, int(num))

print(ans)