n, k = map(int, input().split())
wp = [list(map(int, input().split())) for _ in range(n)]
wp.sort(key=lambda x: -x[1])

ans = 0
for i in range(n):
    print(wp[i],  wp[i][0] * wp[i][1] // 100)
    ans += wp[i][0] * wp[i][1] // 100

print(ans)