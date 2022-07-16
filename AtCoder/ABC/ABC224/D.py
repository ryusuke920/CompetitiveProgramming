import sys
input = sys.stdin.readline

from collections import deque, defaultdict

m = int(input())
g = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]
p = list(map(lambda x: int(x) - 1, input().split()))

# grid[i] := 頂点 i にいるコマ （空白は -1）
# grid[i] = i （grid == goal） となれば終了
grid = [str(0)] * 9
for i in range(8):
    grid[p[i]] = str(i + 1)
    p[i] = str(p[i])

q = deque()
q.append("".join(grid))
goal = "123456780"
d = defaultdict(int)
d["".join(grid)] = 1

if "".join(grid) == goal:
    exit(print(0))

cnt = 0
while q:

    prev_list = q.popleft()

    if cnt >= 3 * 10 ** 6:
        break

    for u, v in g:

        nxt_list = [i for i in prev_list]
        if not (nxt_list[u] == '0' or nxt_list[v] == '0'):
            continue
        nxt_list[u], nxt_list[v] = nxt_list[v], nxt_list[u]

        if d["".join(nxt_list)] == 0:

            d["".join(nxt_list)] = d["".join(prev_list)] + 1
            
            q.append("".join(nxt_list))
            cnt += 1

            if "".join(nxt_list) == goal:
                exit(print(d["".join(goal)] - 1))

print(-1)