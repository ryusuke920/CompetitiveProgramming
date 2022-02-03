n = int(input())
ch = [[] for i in range(n)]
for i in range(n):
    a,b = map(str,input().split())
    ch[i].append((a,b,1))

m = int(input())
ans = ""
for i in range(m):
    x = input()
    if ch[0] in 