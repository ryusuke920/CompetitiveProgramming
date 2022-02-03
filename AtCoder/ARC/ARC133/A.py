n = int(input())
a = list(map(int, input().split()))

cnt = a[-1]
for i in range(n - 1):
    if a[i] > a[i + 1]:
        cnt = a[i]
        break

ans = []
for i in a:
    if i != cnt:
        ans.append(i)

print(*ans)