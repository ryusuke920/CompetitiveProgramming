r, x, y = map(int,input().split())
i = 1
while True:
    if x ** 2 + y ** 2 <= (r * i) ** 2:
        if i == 1:
            if x ** 2 + y ** 2 == r ** 2:
                exit(print(1))
            else:
                exit(print(2))
        else:
            exit(print(i))
    i += 1