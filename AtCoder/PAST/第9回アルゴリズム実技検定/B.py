ans = 0
for _ in range(int(input())):
    x, y = map(int, input().split())
    oturi = y - x

    a = oturi // 500
    oturi -= 500 * a

    b = oturi // 100
    oturi -= 100 * b

    c = oturi // 50
    oturi -= 50 * c

    d = oturi // 10
    oturi -= 10 * d

    e = oturi // 5
    oturi -= 5 * e

    f = oturi // 1
    oturi -= 1 * f

    ans += c + e

print(ans)