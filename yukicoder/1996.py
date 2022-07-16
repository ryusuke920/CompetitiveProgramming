n, k = map(int, input().split())
a = list(map(int, input().split()))
s = list(input())
t = []
for i in s:
    if i == '<':
        t.append(1)
    else:
        t.append(0)

start = a[0]
same = 1
u = []
for i in range(1, n):
    if start == a[i]:
        same += 1
    elif start < a[i]:
        u.append((same, 1))
        same = 1
        start = a[i]
    elif start > a[i]:
        u.append((same, 0))
        same = 1
        start = a[i]

mod = 10 ** 9 + 7
print(t)
print(*u)