from math import log2
n, m, d = map(int,input().split())
a = list(map(int,input().split()))[::-1]
doub = int(log2(d)) + 2
kuzi = [[i for i in range(n + 1)] for _ in range(doub)]

for i in a:
    kuzi[1][i], kuzi[1][i + 1] = kuzi[1][i + 1], kuzi[1][i]

num = [0] * (n + 1)
for i, j in enumerate(kuzi[1]):
    if i == 0: continue
    num[j] = i
kuzi[1] = num

for i in range(2, doub):
    for j in range(1, n + 1):
        kuzi[i][j] = kuzi[i - 1][kuzi[i - 1][j]]

x = [int(i) for i in bin(d)[2:]]
for i in range(1, n + 1):
    ans = i
    for j in range(len(x)):
        if x[j]:
            ans = kuzi[len(x) - j][ans]

    print(ans)