v, a, b, c = map(int, input().split())

i = 0
while True:
    if i % 3 == 0:
        v -= a
    elif i % 3 == 1:
        v -= b
    elif i % 3 == 2:
        v -= c
    
    if v < 0:
        if i % 3 == 0:
            print('F')
        elif i % 3 == 1:
            print('M')
        elif i % 3 == 2:
            print('T')
        exit()
    i += 1