def CC(A: list) -> list:
    "座標圧縮"
    B = {j: i for i, j in enumerate(A)}
    return B

n, k = map(int,input().split())
a = list(map(int,input().split()))
ans = cnt = 0
p = k // n
num = [p] * n

cnt = CC(a)
r = k - p * n

kankei = []
for i in range(n):
    kankei.append([cnt[a[i]], a[i]])
kankei.sort(key = lambda x: x[1])

for i in range(r):
    num[kankei[i][0]] += 1

for i in range(n):
    print(num[i])