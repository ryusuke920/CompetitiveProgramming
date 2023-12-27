import sys
input = sys.stdin.readline
from collections import deque

def main() -> None:
    n = int(input())
    g = [[] for _ in range(n)]
    for i in range(n):
        c, *p = map(int, input().split())
        for j in range(c):
            g[i].append(p[j] - 1)
    

    q = deque([0])
    s = set()
    s.add(0)
    ans = [1]
    while q:
        v = q.popleft()
        for nxt in g[v]:
            if nxt not in s:
                s.add(nxt)
                q.append(nxt)
                ans.append(nxt + 1)
    
    print(*ans[::-1][:-1])

if __name__ == "__main__":
    main()