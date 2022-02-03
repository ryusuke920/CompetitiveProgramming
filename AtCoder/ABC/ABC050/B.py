n = int(input())
t = list(map(int,input().split()))
m = int(input())
for i in range(m):
    p,x = map(int,input().split())
    print(sum(t) + (x-t[p-1]))