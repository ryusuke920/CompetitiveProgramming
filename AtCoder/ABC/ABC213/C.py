def CC(A: list) -> list:
    "座標圧縮"
    B = {j: i + 1 for i, j in enumerate(sorted(set(A)))}
    return B

h, w, n = map(int,input().split())
a, b = [0] * n, [0] * n
for i in range(n):
    a[i], b[i] = map(int,input().split())

num_a = CC(a)
num_b = CC(b)

for i in range(n):
    print(num_a[a[i]], num_b[b[i]])