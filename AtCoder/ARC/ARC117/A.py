a, b =map(int,input().split()) # +,-
ans = []
if a == b:
    for i in range(a):
        ans.append(i + 1)
    for i in range(b):
        ans.append(-(i + 1))
    print(*ans)
elif a > b:
    for i in range(a):
        ans.append(i + 1)
    for i in range(b - 1):
        ans.append(-(i + 1))
    x = a * (a + 1)// 2
    y = b * (b - 1) // 2
    z = x - y
    ans.append(-z)
    print(*ans)
elif b > a:
    for i in range(b):
        ans.append(-(i + 1))
    for i in range(a - 1):
        ans.append((i + 1))
    x = b * (b + 1)// 2
    y = a * (a - 1) // 2
    z = x - y
    ans.append(z)
    print(*ans)