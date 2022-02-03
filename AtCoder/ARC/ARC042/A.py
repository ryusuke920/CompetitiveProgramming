n,m = map(int,input().split())
yes = {}
a = [int(input()) for _ in range(m)]
a = a[::-1]
for i in range(m):
    yes[a[i]] = 1
no = [0]*n
for i in yes:
    no[i-1] = 1

for i in yes:
    print(i)
for i in range(n):
    if no[i] == 0:
        print(i+1)