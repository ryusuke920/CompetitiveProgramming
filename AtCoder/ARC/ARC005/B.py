x, y, w = input().split()
l = [input() for _ in range(9)]
x = int(x) - 1
y = int(y) - 1
dx, dy = 0, 0
if "R" in w: dx = 1
elif "L" in w: dx = -1
if "U" in w: dy = -1
elif "D" in w: dy = 1

ans=[]
for i in range(4):
    ans.append(l[y][x])
    if x==0 and dx == -1 or x == 8 and dx==1: dx *= -1
    if y==0 and dy == -1 or y == 8 and dy==1: dy *= -1
    x += dx
    y += dy

print("".join(ans))