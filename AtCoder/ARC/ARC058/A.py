n,k = map(str,input().split())
d = list(map(int,input().split()))
d = set(d)
while True:
    if n in d:
        n = int(n)
        n += 1
        n = str(n)
    else:
        print(n)
        break
    print(n)
    if int(n) >= 10000:
        break