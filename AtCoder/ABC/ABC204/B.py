n = int(input())
#x, y = map(int,input().split())
a = list(map(int,input().split()))
ans = cnt = 0
for i in range(n):
    if a[i] >= 10:
        ans += a[i] - 10
print(ans)