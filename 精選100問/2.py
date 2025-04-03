#2020/11/5
n = int(input())
cnt = 0
for i in range(1, n + 1, 2):
    ans = []
    for j in range(1, int(i ** 0.5) + 1):
        if i % j == 0:
            ans.append(j)
            if j**2 != i:
                ans.append(i // j)
    if len(ans) == 8:
        ans.sort()
        cnt += 1

print(cnt)