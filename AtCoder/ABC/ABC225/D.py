n, q = map(int,input().split())
l = [[-1, -1] for _ in range(n + 1)]
for _ in range(q):
    a = list(map(int,input().split()))
    if a[0] == 1:
        l[a[1] - 1][1] = a[2]
        l[a[2] - 1][0] = a[1]
    elif a[0] == 2:
        l[a[1] - 1][1] = -1
        l[a[2] - 1][0] = -1
    elif a[0] == 3:
        before = []
        after = []
        now = a[1] - 1
        while True:
            after.append(now + 1)
            if l[now][1] == -1: break
            now = l[now][1] - 1
        
        now = a[1] - 1
        if l[now][0] != -1:
            now = l[now][0] - 1
            while True:
                before.append(now + 1)
                if l[now][0] == -1: break
                now = l[now][0] - 1

        ans = before[::-1] + after
        ans = [len(ans)] + ans
        print(*ans)