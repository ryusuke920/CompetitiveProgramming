n = 2 ** 20

num = {i: 0 for i in range(n)}
a = [-1] * n

q = int(input())
for _ in range(q):
    t, x = map(int,input().split())
    if t == 1:
        h = x % n
        while a[h] != -1:
            cnt = num[h] + 1
            num[h] += 1
            h = (h + cnt) % n
        a[h] = x
    elif t == 2:
        print(a[x % n])