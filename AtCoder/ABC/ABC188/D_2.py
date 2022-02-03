def CC(A: list) -> list:
    "座標圧縮"
    B = {j: i for i, j in enumerate(sorted(set(A)))}
    return B

n, C = map(int,input().split())
a, b, c = [0] * n, [0] * n, [0] * n

for i in range(n):
    a[i], b[i], c[i] = map(int,input().split())
    a[i] -= 1

day = sorted(set((a + b)))

x = CC(day)

money = [0] * len(day)
for i in range(n):
    money[x[a[i]]] += c[i]
    money[x[b[i]]] -= c[i]

for i in range(len(money) - 1):
    money[i + 1] += money[i]

ans = 0
for i in range(len(day) - 1):
    ans += (day[i + 1] - day[i]) * min(C, money[i])

print(ans)