from collections import deque

n = int(input())
a = list(map(int, input().split()))

q = deque()
q.append((a[0], 1))
l = 1
print(1)
for i in range(1, n):
    if l != 0:
        now, cnt = q.pop()
        if now != a[i]:
            q.append((now, cnt))
            q.append((a[i], 1))
            l += 1
        else:
            cnt += 1
            l += 1
            q.append((now, cnt))
            while True:
                now, cnt = q.pop()
                if now != cnt:
                    q.append((now, cnt))
                    break
                l -= now
                if l == 0:
                    break
    else:
        q.append((a[i], 1))
        l += 1

    print(l)