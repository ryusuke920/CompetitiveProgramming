import sys
input = sys.stdin.readline

def f(x: int, y: int) -> bool:
    if s[x][y] == "#":
        return False
    
    for i in range(n):
        if t[i] == "L":
            if y == 0:
                return False
            if s[x][y - 1] == "#":
                return False
            y -= 1
        if t[i] == "R":
            if y == w - 1:
                return False
            if s[x][y + 1] == "#":
                return False
            y += 1
        if t[i] == "U":
            if x == 0:
                return False
            if s[x - 1][y] == "#":
                return False
            x -= 1
        if t[i] == "D":
            if x == h - 1:
                return False
            if s[x + 1][y] == "#":
                return False
            x += 1
    
    return True

h, w, n = map(int, input().split())
t = input()
s = [input() for _ in range(h)]

ans = 0
for i in range(h):
    for j in range(w):
        if s[i][j] == "." and f(i, j):
            ans += 1
    
print(ans)