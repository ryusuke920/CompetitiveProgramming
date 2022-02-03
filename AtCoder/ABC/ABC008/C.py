n = int(input())
c = [int(input()) for _ in range(n)]

ans = 0
for i in range(n):
    s = 0
    for j in range(n):
        if i == j: continue
        if c[i] % c[j] == 0:
            s += 1

    if s % 2:
        ans += 0.5
    else:
        ans += (s + 2) / (2 * s + 2)

print(ans)