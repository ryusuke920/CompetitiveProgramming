from itertools import product
h, w, K = map(int,input().split())
s = [[int(i) for i in input()] for _ in range(h)]

ans = 10 ** 7
for i in product([0, 1], repeat = h - 1):
    I = i.count(1) + 1
    cnt = I - 1
    num = [0] * I
    Bool = True

    for j in range(w):
        t = 0
        for k in range(h):
            if k != 0 and i[k - 1] == 1:
                t += 1
            num[t] += s[k][j]

        if max(num) > K:
            cnt += 1
            num = [0] * I
            t = 0
            for l in range(h):
                if l != 0 and i[l - 1] == 1:
                    t += 1
                num[t] += s[l][j]


            if max(num) > K:
                Bool = False
                break
    if Bool:
        ans = min(ans, cnt)

print(ans)