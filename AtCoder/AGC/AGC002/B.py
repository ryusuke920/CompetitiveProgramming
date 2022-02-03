n,m = map(int,input().split())
x = [0]*m
y = [0]*m
for i in range(m):
    x[i],y[i] = map(int,input().split())
ch = [0]*n
num = [1]*n
ch[0] = 1
for i in range(m):
    num[x[i]-1] -= 1
    num[y[i]-1] += 1
    if ch[x[i]-1] == 1 and num[x[i]-1] == 0:
        ch[x[i]-1] = 0
        ch[y[i]-1] = 1
    elif ch[x[i]-1] == 1:
        ch[y[i]-1] = 1
print(ch.count(1))