from collections import deque
n, d, a = map(int,input().split())
x = [list(map(int,input().split())) for _ in range(n)]
x.sort(key = lambda x: x[0])

q = deque()
ans = dmg = 0
for i, j in x: # 座標・体力
    while q and q[0][0] < i:
        _, v = q.popleft()
        dmg -= v
    
    rem = j - dmg
    if rem <= 0: continue
    k = -(-rem // a)
    ans += k
    dmg += k * a
    q.append((i + 2 * d, k * a))

print(ans)