from collections import deque
r,c = map(int,input().split())
sy,sx = map(int,input().split())
gy,gx = map(int,input().split())
c = [list(input()) for _ in range(r)]
dq = deque([(sy-1,sx-1,0)])

while True:
    y,x,n = dq.popleft()
    if y == gy-1 and x == gx-1:
        print(n)
        break
    elif c[y][x] == ".":
        c[y][x] = "#"
        dq.append([y+1,x,n+1])
        dq.append([y-1,x,n+1])
        dq.append([y,x+1,n+1])
        dq.append([y,x-1,n+1])