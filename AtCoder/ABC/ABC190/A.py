a,b,c = map(int,input().split())
if c == 0:
    turn = 0
    while True:
        if turn == 0:
            if a >= 1:
                a -= 1
                turn = 1
            else:
                exit(print("Aoki"))
        else:
            if b >= 1:
                b -= 1
                turn = 0
            else:
                exit(print("Takahashi"))
else:
    turn = 1
    while True:
        if turn == 0:
            if a >= 1:
                a -= 1
                turn = 1
            else:
                exit(print("Aoki"))
        else:
            if b >= 1:
                b -= 1
                turn = 0
            else:
                exit(print("Takahashi"))