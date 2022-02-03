from collections import deque
n,m  = map(int, input().split())
r = [[] for _ in range(n+1)]
ans = [0]*(n+1)
for i in range(m):
  a,b  = map(int, input().split())
  r[a].append(b)
  r[b].append(a)
 
q = deque([1])
while q:
  fr = q.popleft()
  for i in r[fr]:
    if ans[i] != 0:
      continue
    ans[i] = fr
    q.append(i)
print(ans)
print("Yes")
for i in ans[2:]:
  print(i)