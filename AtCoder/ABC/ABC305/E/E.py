import sys
input = sys.stdin.readline
from collections import deque, defaultdict

def main() -> None:
    n, m, k = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(lambda x: int(x) - 1, input().split())
        g[a].append(b)
        g[b].append(a)

    q = deque()
    d = defaultdict(lambda: 0)
    is_ok = [False] * n
    for _ in range(k):
        p, h = map(int, input().split())
        d[p - 1] = h
        q.append((p - 1, h))
        is_ok[p - 1] = True
        while q:
            vp, vh = q.popleft()
            for nxt in g[vp]:
                if is_ok[nxt]:
                    continue
                is_ok[nxt] = True
                if vh >= 2:
                    if d[nxt] == 0:
                        q.append((nxt, vh - 1))
                    else:
                        q.append((nxt, max(d[nxt], vh - 1)))
    
    ans = []
    for i in range(n):
        if is_ok[i]:
            ans.append(i + 1)
    
    print(len(ans))
    print(*ans)
    

if __name__ == "__main__":
    main()