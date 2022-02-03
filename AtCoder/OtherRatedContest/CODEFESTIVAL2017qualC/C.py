from collections import deque
s = input()
q = deque()
ans = 0
for i in range(len(s)):
    q.append(s[i])
while q:
    if q[0] == q[-1]:
        if len(q) == 1:
            exit(print(ans))
        else:
            q.pop()
            q.popleft()
    else:
        if q[0] == "x":
            q.append("x")
            ans += 1
        elif q[-1] == "x":
            q.appendleft("x")
            ans += 1
        else:
            exit(print(-1))
print(ans)