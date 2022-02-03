b, c = map(int,input().split())
if b == 0 and c == 1:
    print(1)
elif c == 1:
    print(2)
elif (b == 1 and c == 1) or (b == -1 and c == 1):
    print(2)
elif b == 0 and c == 2:
    print(3)
elif 4 * abs(b) <= c:
    if b == 0:
        print(c)
    else:
        if b < 0:
            print(2 * (abs(b)) + 1 + (c - 1) // 2 + c // 2)
        else:
            print(2 * (abs(b)) + 1 + (c - 1) // 2 + (c - 2) // 2)
else:
    if b < 0:
        print(2 + c // 2 + (c - 1) // 2 + (c - 1) // 2 + (c - 2) // 2)
    else:
        print(2 + (c - 1) // 2 + (c - 2) // 2 + min(2 * (b - 1) + 1, (c - 1) // 2 + c // 2))