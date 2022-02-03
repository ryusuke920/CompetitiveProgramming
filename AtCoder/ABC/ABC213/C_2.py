def CC(A: list) -> list:
    "座標圧縮"
    B = {j: i + 1 for i, j in enumerate(sorted(set(A)))}
    return B

h, w, n = map(int,input().split())
a, b = [0] * n, [0] * n
for i in range(n):
    a[i], b[i] = map(int,input().split())
x = CC(a)
y = CC(b)

for i in range(n):
    print(x[a[i]], y[b[i]])