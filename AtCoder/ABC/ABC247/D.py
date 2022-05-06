from collections import deque

q = deque()
for _ in range(int(input())):
    t = list(map(int, input().split()))
    if t[0] == 1:
        q.append((t[1], t[2]))
    elif t[0] == 2:
        num = 0
        cnt = 0
        while True:
            v = q.popleft()
            if cnt + v[1] < t[1]:
                cnt += v[1]
                num += v[0] * v[1]
            else:
                need = t[1] - cnt
                num += v[0] * need
                q.appendleft((v[0], v[1] - need))
                print(num)
                break