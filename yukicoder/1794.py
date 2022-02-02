n, m = map(int, input().split())

ans = []
while True:
    if m == 0:
        break
    p = n // m
    ans.append(p)
    n -= p * m
    n, m = m, n

print(*ans)