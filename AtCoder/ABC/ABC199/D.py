from itertools import product

n, m = map(int,input().split())

g = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int,input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)

check = [0] * n

for i in range(n):
    if check[i] == 0:
        check[i] = 1
        R, g, b = [i], [], []
        q = [i]

        while q:

            v = q.pop()
            Index = r.index(v)

            for i in g[v]:
                if check[i] == 0:
                    g += [[Index, r.index(i)]]
                else:
                    check[i] = 1
                    q += [i]
                    r += [i]
                    b += [Index]
    
    x = 0
    for i in product([0, 1, 2], repeat = n - 1):
        c = []
        for j in range(n - 1):
            c += [(c[b[j]] + i[j]) % 3]

        if all (c[a] != c[b] for a, b in g):
            x += 1

    ans *= 3 * x
print(ans)