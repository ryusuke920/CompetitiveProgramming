n = int(input())
a = [int(input()) for i in range(n)]
ans = []
for i in range(n):
    if a[i] not in ans:
        ans.append(a[i])
ans.sort()
print(ans[-2])