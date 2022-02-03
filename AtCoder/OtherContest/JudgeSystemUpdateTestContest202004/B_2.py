n = int(input())
a = [list(input().split()) for _ in range(n)]
for i in range(n):
    a[i][0] = int(a[i][0])
a.sort()
a.sort(key = lambda x: x[1], reverse = True)
for i in range(n):
    print(a[i][0])