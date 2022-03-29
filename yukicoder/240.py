from collections import defaultdict, deque

X, Y = map(int, input().split())

d = ((-1, -2), (1, -2), (-2, -1), (2, -1), (-2, 1), (2, 1), (-1, 2), (1, 2))

check = defaultdict(int)
check['0_0'] = 1
q = deque()
q.append([0, 0])
for i in range(3):
    q_tmp = deque()
    while q:
        vy, vx = q.popleft()
        for dy, dx in d:
            y = vy + dy
            x = vx + dx
            if check[f'{y}_{x}'] != 0: continue
            check[f'{y}_{x}'] = 1
            q_tmp.append((y, x))
    
    while q_tmp:
        v = q_tmp.popleft()
        q.append(v)

print('YES') if check[f'{Y}_{X}'] else print('NO')