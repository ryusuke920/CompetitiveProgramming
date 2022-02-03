from collections import deque
n, x, y = map(int,input().split())
xy = [list(map(int,input().split())) for _ in range(n)]
q = deque()
q.append((0, 0))
d = (())