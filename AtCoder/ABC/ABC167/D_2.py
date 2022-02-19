n, k = map(int, input().split())
a = list(map(int, input().split()))

dob = [[0] * n for _ in range(60)]

# dob[i][j] := jにいるときに2**i回ループするとどこに行くか
for i in range(n):
    dob[0][i] = a[i] - 1

for i in range(1, 60):
    for j in range(n):
        dob[i][j] = dob[i - 1][dob[i - 1][j]]

a = []
for i in range(60):
    if k >> i & 1:
        a.append(i)

now = 0
for i in a:
    now = dob[i][now]

print(now + 1)