n, m = map(int,input().split())
ab = [[0, 0] for _ in range(m)]
for i in range(m):
    ab[i][0], ab[i][1] = map(int,input().split())
ab.sort(key = lambda x: x[0])

ans, left, right = 1, ab[0][0], ab[0][1]
for i in range(m - 1):
    if left <= ab[i + 1][0] and right >= ab[i + 1][1]:
        left = ab[i + 1][0]
        right = ab[i + 1][1]
    elif left > ab[i + 1][1]:
        ans += 1
        left = ab[i + 1][0]
        right = ab[i + 1][1]
    elif left <= ab[i + 1][1] and left > ab[i + 1][0]:
        right = ab[i + 1][1]
    elif right > ab[i + 1][0] and right < ab[i + 1][1]:
        left = ab[i + 1][0]
    elif right <= ab[i + 1][0]:
        ans += 1
        left = ab[i + 1][0]
        right = ab[i + 1][1]
print(ans)