from collections import deque
s = list(input())
ans = ["".join(s)]
q = deque()
for i in s:
    q.append(i)

for i in range(len(s) - 1):
    t = q.popleft()
    q.append(t)
    ans.append("".join(q))
ans.sort()
print(ans[0])
print(ans[-1])