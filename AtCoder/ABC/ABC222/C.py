n, m = map(int, input().split())
a, ans = [], []
t = 2 * n

for i in range(t):
    a.append(list(input()))
    ans.append([0, i])

for i in range(m):
    cnt = [0] * t
    for j in range(0, t, 2):
        if a[ans[j][1]][i] == 'G':
            if a[ans[j + 1][1]][i] == 'C': ans[j][0] += 1
            elif a[ans[j + 1][1]][i] == 'P': ans[j + 1][0] += 1
        elif a[ans[j][1]][i] == 'C':
            if a[ans[j + 1][1]][i] == 'G': ans[j + 1][0] += 1
            elif a[ans[j + 1][1]][i] == 'P': ans[j][0] += 1
        else:
            if a[ans[j + 1][1]][i] == 'G': ans[j][0] += 1
            elif a[ans[j + 1][1]][i] == 'C': ans[j + 1][0] += 1

    ans.sort(key=lambda x: x[1])
    ans.sort(reverse=True, key=lambda x: x[0])

for i, j in ans: print(j + 1)