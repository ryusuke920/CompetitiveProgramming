n, k = map(int,input().split())
p = [list(map(int,input().split())) for _ in range(n)]

a = []
for i in range(n):
    a.append(sum(p[i]))
a.sort(reverse=True)

cnt = a[k - 1]
for i in range(n):
    if sum(p[i]) + 300 >= cnt:
        print("Yes")
    else:
        print("No")