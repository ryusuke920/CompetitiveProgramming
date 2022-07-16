
n, q = map(int, input().split())
s = list(input())

cnt = 0
for i in range(q):
    t, x = map(int, input().split())
    if t == 1:
        cnt += x
    elif t == 2:
        print(s[(-cnt + x - 1) % n])