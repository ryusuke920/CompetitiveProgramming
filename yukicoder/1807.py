n = int(input())
p = float(input())

if n >= 200:
    print(1)
else:
    ans = p
    cnt = 1 - p
    for i in range(2, n + 1):
        ans += cnt * p
        cnt *= (1 - p)
    print(ans)