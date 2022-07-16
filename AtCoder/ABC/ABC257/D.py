import sys
input = sys.stdin.readline
from collections import deque

def bfs(start: int, s: int) -> bool:

    q = deque([start])
    bool = [False] * n
    bool[start] = True

    while q:

        i = q.popleft()

        for j in range(n):

            if bool[j]:
                continue

            if not (p[i] * s >= dist[i][j]):
                continue

            bool[j] = True
            q.append(j)

    return True if bool.count(True) == n else False


def check(S: int) -> bool:

    bool = False

    for start in range(n):
        if bfs(start, S):
            bool = True
            break

    return bool


def binary_search(left: int, right: int) -> int:
    while right - left > 1:
        mid = (left + right) // 2
        if check(mid):
            right = mid
        else:
            left = mid

    return right


n = int(input())
x, y, p = [0] * n, [0] * n, [0] * n
for i in range(n):
    x[i], y[i], p[i] = map(int, input().split())


INF = 10 ** 18
dist = [[INF] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        dist[i][j] = abs(x[i] - x[j]) + abs(y[i] - y[j])

print(binary_search(-1, INF))