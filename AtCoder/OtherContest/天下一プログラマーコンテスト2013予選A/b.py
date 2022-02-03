n = int(input())
ans = 0
for i in range(n):
    a = list(map(int,input().split()))
    if 0 <= sum(a) < 20:
        ans += 1
print(ans)