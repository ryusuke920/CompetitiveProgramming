from collections import deque

n = int(input())
s = input()
t = deque([])
for i in s:
    if i != 'A':
        t.append(i)
    else:
        t.append('B')
        t.append('B')

l = len(t)
ans = []
while l >= 2:
    u = t.popleft()
    v = t.popleft()
    if u == v and u == 'B':
        ans.append('A')
        l -= 2
    else:
        ans.append(u)
        t.appendleft(v)
        l -= 1

for i in t:
    ans.append(i)

print(''.join(ans))