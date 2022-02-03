n = int(input())
a = [int(input()) for i in range(n)]
ans = set([])
for i in range(n):
    if a[i] in ans:
        ans.remove(a[i])
    else:
        ans.add(a[i])
print(len(ans))