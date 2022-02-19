s = input()
n = len(s)

dob = [[0] * n for _ in range(60)]
for i in range(n):
    if s[i] == 'L':
        dob[0][i] = i - 1
    else:
        dob[0][i] = i + 1

for i in range(1, 60):
    for j in range(n):
        dob[i][j] = dob[i - 1][dob[i - 1][j]]

ans = [0] * n
for i in range(n):
    ans[dob[-1][i]] += 1

print(*ans)