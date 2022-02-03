def CC(A: list) -> list:
    "座標圧縮"
    B = {j: i for i, j in enumerate(sorted(set(A)))}
    return B

def C(A: list) -> list:
    "座標圧縮"
    B = {i: j for i, j in enumerate(sorted(set(A)))}
    return B

n = int(input())
a, b = [0] * n, [0] * n
c = [0] * n
for i in range(n):
    a[i], b[i] = map(int,input().split())
    c[i] = a[i] + b[i]

day = sorted(set(a + c))
x = CC(day)
y = C(day)

cnt = [0] * len(x)
for i in range(n):
    cnt[x[a[i]]] += 1
    cnt[x[c[i]]] -= 1

for i in range(len(cnt) - 1):
    cnt[i + 1] += cnt[i]

d = [0] * (n + 1) # d[i] := i日めのログイン人数

for i, j in enumerate(cnt):
    try:
        d[j] += max(0, y[i + 1] - y[i])
    except:
        KeyError
print(*d[1:], sep=" ")