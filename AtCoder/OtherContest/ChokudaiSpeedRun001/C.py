n = int(input())
a = list(map(int,input().split()))
ans = []
for i in range(n):
    ans .append(a[i])
    ans.append(",")
print(*ans[:-1], sep = "")