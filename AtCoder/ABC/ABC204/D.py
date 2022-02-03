n = int(input())
t = list(map(int,input().split()))
s = sum(t)

Bool = [0] * (10 ** 5 + 1)
for i in range(n):
    for j in range(10 ** 5, -1, -1):
        if Bool[j] == 1:
            Bool[j + t[i]] = 1
    Bool[t[i]] = 1

ans = []
for i in range(10 ** 5 + 1):
    if Bool[i] == 1:
        ans.append(abs(s - 2 * i))

ans.sort()
print(ans)
print((s + ans[0]) // 2)