n = int(input())
a = [0]*6
for i in range(n):
    x,y = map(float,input().split())
    if x >= 35:
        a[0] += 1
    if x >= 30 and x < 35:
        a[1] += 1
    if x >= 25 and x < 30:
        a[2] += 1
    if y >= 25:
        a[3] += 1
    if x >= 0 and y < 0:
        a[4] += 1
    if x < 0:
        a[5] += 1
print(*a)