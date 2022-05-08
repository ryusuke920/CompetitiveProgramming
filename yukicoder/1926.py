for _ in range(int(input())):
    n, m, k = map(int, input().split())
    r = k % m
    if m - r <= n:
        print(0)
    else:
        print(k % m)