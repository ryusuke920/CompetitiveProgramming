n = int(input())
a = list(map(int,input().split()))
x1 = sum(a) - 2*sum(a[1::2])
ans = [x1]
for i in range(n-1):
    x = 2*a[i] - ans[i]
    ans.append(x)
print(*ans)