m, n = map(int,input().split())
if m == 0:
    print(n + 1)
elif m == 1:
    print(n + 2)
elif m == 2:
    print(2 * n + 3)
else:
    print(2 ** (n + 3) - 3)