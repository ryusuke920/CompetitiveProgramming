n = int(input())
x = list(map(int,input().split()))
a = sorted(x)
front = a[n//2-1]
rear = a[n//2]
for i in x:
    if i <= front:
        print(rear)
    else:
        print(front)