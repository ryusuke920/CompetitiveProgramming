n = int(input())
ans = 0
for i in range(n):
    mi, ma = map(int,input().split())
    ans = max(0, ma - 2 * mi + 1)
    print(ans * (ans + 1) // 2)