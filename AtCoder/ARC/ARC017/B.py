n, k = map(int,input().split())
a = [int(input()) for _ in range(n)]
ans = cnt = 0
for i in range(n - 1):
    if a[i] < a[i + 1]:
        cnt += 1
    else:
        ans += max(0, cnt - k + 2)
        cnt = 0
ans += max(0, cnt - k + 2)
print(ans)