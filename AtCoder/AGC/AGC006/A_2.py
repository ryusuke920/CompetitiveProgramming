from collections import deque
n = int(input())
s = input()
t = input()
if s == t:
    exit(print(n))
a, b = deque(), deque()
for i in s:
    a.append(i)
for i in t:
    b.append(i)

num = 0
while True:
    if len(a) >= 1 and len(b) >= 1:
        if a[-1] == b[0]:
            a.pop()
            b.popleft()
            num += 1
        else:
            break
    else:
        break

print(n * 2 - num)