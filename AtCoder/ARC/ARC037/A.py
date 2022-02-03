n = int(input())
m = list(map(int,input().split()))
ans = 0
for i in range(n):
    if m[i] <= 80:
        ans += 80-m[i]
print(ans)