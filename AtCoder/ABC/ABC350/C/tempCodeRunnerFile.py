n = int(input())
a = list(map(int, input().split()))

ans = []
num = [0]*(n + 1)
for i in range(n):
    num[a[i]] = i

for i in range(n):
    if a[i] == i + 1:
        continue
    else:
        l, r = i, num[i + 1]
        x, y = a[i], i + 1
        a[l], a[r] = a[r], a[l]
        num[x], num[y] = num[y], num[x]
        ans.append((l + 1, r + 1))

print(len(ans))
for i in ans:
    print(i[0], i[1])