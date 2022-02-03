from collections import deque, defaultdict
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
d = defaultdict(int)
# ontop[i] := １番上にある色iの個数の集合
ontop = [[] for _ in range(n)]

a = []
for i in range(m):
    int(input())
    # pop()するために逆順
    a.append(list(map(int,input().split()))[::-1])
    ontop[a[i][-1] - 1].append(i)

# q := １番上に２個同じものがある集合
q = deque()
for i in range(n):
    if len(ontop[i]) == 2:
        q.append(i)

cnt = 0
while q:
    color = q.popleft()
    cnt += 1
    x, y = ontop[color]

    a[x].pop()
    if len(a[x]):
        new_color = a[x][-1] - 1
        ontop[new_color].append(x)
        if len(ontop[new_color]) == 2:
            q.append(new_color)

    a[y].pop()
    if len(a[y]):
        new_color = a[y][-1] - 1
        ontop[new_color].append(y)
        if len(ontop[new_color]) == 2:
            q.append(new_color)

if cnt == n:
    print("Yes")
else:
    print("No")