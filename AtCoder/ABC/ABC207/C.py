n = int(input())
ans = 0
t, l, r = [0] * n, [0] * n, [0] * n
for i in range(n):
    t[i], l[i], r[i] = map(int,input().split())

for i in range(n):
    for j in range(n):
        if i == j: continue
        li, ri, lj, rj = l[i], r[i], l[j], r[j]

        if t[i] == 2:
            ri -= 0.01
        if t[j] == 2:
            rj -= 0.01
        if t[i] == 3:
            li += 0.01
        if t[j] == 3:
            lj += 0.01
        if t[i] == 4:
            li += 0.01
            ri -= 0.01
        if t[j] == 4:
            lj += 0.01
            rj -= 0.01
        if max(li, lj) <= min(ri, rj):
            ans += 1
print(ans // 2)