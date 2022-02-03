n,k = map(int,input().split())
a = [int(input()) for _ in range(n)]
ans = 0
for i in range(n):
    ans += a[i]
    if ans >= k:
        print(i+1)
        break