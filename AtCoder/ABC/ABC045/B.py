sa = str(input())
sb = str(input())
sc = str(input())
turn = 1
while True:
    if turn == 1 and len(sa) == 0:
        print("A")
        break
    elif turn == 2 and len(sb) == 0:
        print("B")
        break
    elif turn == 3 and len(sc) == 0:
        print("C")
        break
    if turn == 1:
        if sa[0] == "a":
            turn = 1
        elif sa[0] == "b":
            turn = 2
        else:
            turn = 3
        sa = sa[1:]
    elif turn == 2:
        if sb[0] == "a":
            turn = 1
        elif sb[0] == "b":
            turn = 2
        else:
            turn = 3
        sb = sb[1:]
    else:
        if sc[0] == "a":
            turn = 1
        elif sc[0] == "b":
            turn = 2
        else:
            turn = 3
        sc = sc[1:]