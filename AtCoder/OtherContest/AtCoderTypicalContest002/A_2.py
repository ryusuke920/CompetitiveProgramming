H,W=map(int,input().split());a,b=map(int,input().split());c,d=map(int,input().split());a-=1;b-=1;from collections import*;q=deque();q.append((a,b));G=[list(input()) for _ in range(H)];t=[[-1]*W for _ in range(H)];t[a][b]=0
while q:
    e,f=q.popleft()
    for g,h in ((0,1),(0,-1),(1,0),(-1,0)):
        y=e+h;x=f+g
        if not(0<=x<W and 0<=y<H)or G[y][x]=="#"or t[y][x]!=-1:continue
        t[y][x]=t[e][f]+1;q.append((y,x))
print(t[c-1][d-1])