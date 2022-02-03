n = int(input())
d = [int(input()) for i in range(n)]
ans = []
for i in range(n):
    if d[i] not in ans:
        ans.append(d[i])
print(len(ans))