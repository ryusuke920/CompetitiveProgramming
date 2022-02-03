a,b = map(int,input().split())
n = 1
ans = 0
while True:
    n += 1
    if (int(n*0.08) == a and int(n*0.10) == b):
        print(n)
        break
    if n >= (a+1)*10 and n >= (b+1)*10:
        print(-1)
        break