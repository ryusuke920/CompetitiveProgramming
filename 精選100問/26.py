from collections import deque
n, q = map(int,input().split())
graph = [[] for _ in range(n)] # 隣接行列の作成
for i in range(n - 1):
    a, b = map(int,input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

ans = [0] * n # 答えとなるカウンターの値
for i in range(q):
    p, x = map(int,input().split())
    ans[p - 1] += x

q = deque()
q.append(0)
check = [0] * n
while q:
    v = q.popleft()
    check[v] = 1 # queueに入ってるノードをチェック済みにする
    for i in graph[v]:
        if check[i] != 0: continue # 未チェックの状態なら調べ上げる
        ans[i] += ans[v]
        q.append(i)
print(*ans)