a = [list(map(int,input().split())) for _ in range(3)]
for i in range(4):
    x1 = i
    y1 = a[0][0] - x1
    x2 = a[1][0] - y1
    x3 = a[2][0] - y1
    y2 = a[0][1] - x1
    y3 = a[0][2] - x1
    if x1+y1 == a[0][0] and x1+y2 == a[0][1] and x1+y3 == a[0][2] and x2+y1 == a[1][0] and x2+y2 == a[1][1] and x2+y3 == a[1][2] and x3+y1 == a[2][0] and x3+y2 == a[2][1] and x3+y3 == a[2][2]:
        print("Yes")
        exit()
print("No")