a,b,c = map(int,input().split())
while True:
    if a <= b * c:
        exit(print(a/b))
    else:
        a -= 1