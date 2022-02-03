from collections import deque
n = int(input())
g = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int,input().split())
    g[a - 1].append((b - 1, i)) # 繋がってるノード・何番目
    g[b - 1].append((a - 1, i)) # 繋がってるノード・何番目

q = deque()
q.append((0, 0)) # ノード・０番目
color = [0] * (n - 1)
while q:
    v1, v2 = q.popleft() # 今いるノード・何番目
    c = 1
    for i, j in g[v1]: # 新しいノード・何番目
        if color[j] == 0:
            if c == v2:
                c += 1
            color[j] = c
            q.append((i, c)) #新しいノード・何番目
            c += 1

print(max(color))
print(*color, sep = "\n")