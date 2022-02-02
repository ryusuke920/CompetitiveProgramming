from collections import deque

k = int(input())

q_0 = deque()
q_1 = deque()
q_2 = deque()
q_3 = deque()

q_0.append('A')
q_0.append('E')
q_1.append('B')
q_2.append('C')
q_3.append('D')

for i in range(k):
    t = i % 4
    if t == 0:
        q_1.append(q_0.popleft())
    if t == 1:
        q_2.append(q_1.popleft())
    if t == 2:
        q_3.append(q_2.popleft())
    if t == 3:
        q_0.append(q_3.popleft())

print(*q_0, sep='')
print(*q_1, sep='')
print(*q_2, sep='')
print(*q_3, sep='')