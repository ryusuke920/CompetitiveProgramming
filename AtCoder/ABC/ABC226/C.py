from collections import deque

n = int(input())
l = [list(map(int,input().split())) for _ in range(n)]

q = deque()
q.append(l[-1])

Bool = [False] * n
Bool[-1] = True
ans = l[-1][0]
while q:
    v = q.popleft()
    for i in range(v[1]):
        if not Bool[v[i + 2] - 1]:
            ans += l[v[i + 2] - 1][0]
            Bool[v[i + 2] - 1] = True
            q.append(l[v[i + 2] - 1])

print(ans)