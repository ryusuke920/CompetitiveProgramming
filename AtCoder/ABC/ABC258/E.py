n, q, x = list(map(int, input().split()))
w = list(map(int, input().split())) * 2
a = sum(w) // 2
c = x // a * n
x %= a
b = [c for _ in range(n)]
l = -1
r = -1
a = w[-1]
c = [0 for _ in range(n)]
for i in range(n):
    a -= w[l]
    l += 1
    while a < x:
        r += 1
        a += w[r]
    b[i] += r - l + 1
    c[i] = (r + 1) % n
a = {0}
d = 0
e = [0]
while c[d] not in a:
    d = c[d]
    a.add(d)
    e.append(d)
a = e.index(c[d])
d = len(e) - a
for i in range(q):
    k = int(input())
    if k > a:
        k -= a
        if k % d == 0:
            k = d - 1
        else:
            k %= d
            k -= 1
        print(b[e[a + k]])
    else:
        print(b[e[k - 1]])