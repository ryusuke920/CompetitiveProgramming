from collections import deque

n = int(input())
s = input()[::-1]

q = deque()
q.append(n)
for i, j in enumerate(s):
    if j == 'R':
        q.appendleft(n - i - 1)
    elif j == 'L':
        q.append(n - i - 1)

print(*q)