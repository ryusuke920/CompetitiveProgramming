from collections import deque
n,m = map(int,input().split())
neighbor = [[] for _ in range(n)]
dist = [-1] * n
dist[0] = 0 # １つ目の町は０でいける
already_visited = deque()
already_visited.append(0) # start is town of 0
for i in range(m):
    a, b = map(int,input().split())
    neighbor[a - 1].append(b - 1)
    neighbor[b - 1].append(a - 1)

while already_visited:
    x = already_visited.popleft()
    for i in neighbor[x]:
        if dist[i] != -1: continue
        dist[i] = x + 1
        already_visited.append(i)
print("Yes")
print(*dist[1:], sep = "\n")