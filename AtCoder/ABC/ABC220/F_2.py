from collections import deque
from sys import setrecursionlimit
import sys
input = sys.stdin.readline
setrecursionlimit(10 ** 7)

def sub_tree(now: int) -> int:
    if size_child[now]: return size_child[now]
    size_child[now] = 1
    for nxt in g[now]:
        if size_child[nxt]: continue
        size_child[now] += sub_tree(nxt)

    return size_child[now]

n = int(input())
g = [[] for _ in range(n)]
for _ in range(n - 1):
    x, y = map(int,input().split())
    g[x - 1].append(y - 1)
    g[y - 1].append(x - 1)

size_child = [0] * n
sub_tree(0)
dist_zero = sum(size_child) - n

ans = [dist_zero] * n
check = [0] * n
q = deque()
q.append((0, -1))

while q:
    now, past = q.popleft()
    check[now] = 1
    if now: # 0以外
        cnt = ans[past]
        cnt -= size_child[now]
        cnt += n - size_child[now]
        ans[now] = cnt
    
    for nxt in g[now]:
        if check[nxt]: continue
        q.append((nxt, now))

print(*ans, sep="\n")