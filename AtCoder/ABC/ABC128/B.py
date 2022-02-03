n = int(input())
l = []
for i in range(n):
    s,p = map(str,input().split())
    l.append([s,int(p),i+1])
l.sort(key = lambda x: (x[0], -x[1]))
for i in range(n):
    print(l[i][2])