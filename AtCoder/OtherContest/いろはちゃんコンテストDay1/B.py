from collections import deque
s = input()
k = int(input())
q = deque()
for i in s:
    q.append(i)

for i in range(k):
    x = q.popleft()
    q.append(x)

print("".join(q))