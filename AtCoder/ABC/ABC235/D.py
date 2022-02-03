from collections import deque

a, n = map(int, input().split())

q = deque()
q.append((n, 0))

check = set()
check.add(n)

INF = 10 ** 18
ans = INF

while q:
    x, y = q.popleft()

    if x == 1: exit(print(y))
 
    if x >= 10 and x % 10 != 0:
        c = str(x)
        cc = 0
        if c[1] != '0':
            cc = int(c[1:] + c[0])
        if cc not in check and cc != 0:
            check.add(cc)
            q.append((cc, y + 1))

    if x % a == 0 and (x // a) not in check:
        check.add(x // a)
        q.append((x // a, y + 1))

print(-1)