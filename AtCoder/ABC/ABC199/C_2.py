n = int(input())
s = list(input().rstrip())
q = int(input())

turn = 0
for _ in range(q):
    t, a, b = map(int,input().split())
    if t == 1:
        if turn == 0:
            s[a - 1], s[b - 1] = s[b - 1], s[a - 1]
        elif turn == 1:
            x, y = a + n - 1, b + n - 1
            s[x % (2 * n)], s[y % (2 * n)] = s[y % (2 * n)], s[x % (2 * n)]
    elif t == 2:
        turn ^= 1

if turn:
    print(*s[n:] + s[:n], sep = "")
else:
    print(*s, sep = "")