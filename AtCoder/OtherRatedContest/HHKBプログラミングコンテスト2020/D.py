t = int(input())
for i in range(t):
    n,a,b = map(int,input().split())
    if a+b > n:
        print(0)
    else:
        if a > b:
            tmp = a:
            a = b
            b = tmp
        #a < bになった
        