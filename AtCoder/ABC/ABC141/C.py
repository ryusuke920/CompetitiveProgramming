n,k,q = map(int,input().split())
a = [int(input()) for _ in range(q)]
point = [0]*n
for i in range(q):
    point[a[i]-1] += 1
for i in range(n):
    if point[i] > q-k:
        print("Yes")
    else:
        print("No")