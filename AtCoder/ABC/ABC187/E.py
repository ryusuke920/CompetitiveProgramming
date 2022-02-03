n = int(input())
g = [[] for _ in range(n)]
ab = [[0, 0] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int,input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)
    ab[i][0], ab[i][1] = a - 1, b - 1 # 0index

depth = [-1] * n
depth[0] = 0
q = [0]
while q:
    v = q.pop()
    for i in g[v]:
        if depth[i] == -1:
            depth[i] = depth[v] + 1
            q.append(i)

wa = [0] * n
Q = int(input())
for i in range(Q):
    t, e, x = map(int,input().split())
    e -= 1 # 0index
    a, b = ab[e]
    if depth[a] > depth[b]: # bの深さの方が深くなるようにする
        a, b = b, a
        t ^= 3 # 1 -> 2, 2 -> 1
    if t == 1:
        wa[0] += x
        wa[b] -= x
    else: # t == 2:
        wa[b] += x

q = [0]
while q:
    v = q.pop()
    for i in g[v]:
        if depth[i] > depth[v]: # 自分のいる頂点の方が深い場所にある時
            wa[i] += wa[v] # 根の奴らに和を取っていく
            q.append(i) # qに追加する

print(*wa, sep = "\n")