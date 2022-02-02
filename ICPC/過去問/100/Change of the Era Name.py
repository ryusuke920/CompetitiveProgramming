while True:
    a = list(map(str,input().split()))
    if a[0] == "#":
        break
    a[1], a[2], a[3] = int(a[1]), int(a[2]), int(a[3])
    if (a[1] == 31 and a[2] >= 5) or a[1] >= 32:
        print("?",a[1]-30,a[2],a[3])
    else:
        print(a[0],a[1],a[2],a[3])