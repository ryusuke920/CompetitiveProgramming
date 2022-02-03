n = int(input())
for i in range(n):
    a,b = map(int,input().split())
    if abs(a-b) == 0:
        print(-1)
    else:
        print(abs(a-b))