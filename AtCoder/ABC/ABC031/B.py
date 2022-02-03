l,h = map(int,input().split())
n = int(input())
a = [int(input()) for i in range(n)]
for i in range(n):
    if a[i] >= l and a[i] <= h:
        print(0)
    elif a[i] > h:
        print(-1)
    else:
        print(l-a[i])