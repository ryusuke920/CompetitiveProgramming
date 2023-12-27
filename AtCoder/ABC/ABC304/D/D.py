import sys
input = sys.stdin.readline

from collections import deque

def main() -> None:
    n, d = map(int, input().split())
    x, y = [0] * n, [0] * n
    for i in range(n):
        x[i], y[i] = map(int, input().split())
    
    out = [False] * n
    out[0] = True
    q = deque([0])
    while q:
        v = q.popleft()
        for i in range(n):
            if out[i]:
                continue
            dist = (x[i] - x[v]) ** 2 + (y[i] - y[v]) ** 2
            if dist <= d ** 2:
                out[i] = True
                q.append(i)
    
    for i in range(n):
        if out[i]:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()