from collections import deque, defaultdict

N, K = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(N - 1)]
V = list(map(int, input().split()))

graph = defaultdict(list)
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

need = set(V)

l = [0] * (N + 1)
for u in range(1, N + 1):
    l[u] = len(graph[u])

queue = deque()
for i in range(1, N + 1):
    if l[i] == 1 and i not in need:
        queue.append(i)

out = [False] * (N + 1)
while queue:
    node = queue.popleft()
    out[node] = True
    for nxt in graph[node]:
        if not out[nxt]:
            l[nxt] -= 1
            if l[nxt] == 1 and nxt not in need:
                queue.append(nxt)

ans = 0
for i in range(1, N + 1):
    if not out[i]:
        ans += 1

print(ans)