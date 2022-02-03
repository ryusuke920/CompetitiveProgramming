t = int(input())
for _ in range(t):
    ans = 0
    z, y, x = map(int,input().split())
    y //= 2
    if x < y:
        cnt = x
        ans += x
        y -= cnt
        cnt = min(y, z // 2)
        ans += cnt
        z -= cnt * 2
    elif x > y:
        cnt = y
        ans += y
        x -= cnt
        cnt = min(x // 2, z)
        ans += cnt
        x -= cnt * 2
        z -= cnt
        cnt = min(x, z // 3)
        ans += cnt
        z -= cnt * 3
    else:
        ans += x
    ans += z // 5
    print(ans)