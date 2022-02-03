n = int(input())
a = list(map(int,input().split()))
ans = 0
for i in range(n):
    ans += 1 / a[i]
print(1 / ans)