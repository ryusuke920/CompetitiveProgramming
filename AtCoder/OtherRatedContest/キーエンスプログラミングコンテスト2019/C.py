n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
ans = 0
c = [0]*n
if sum(a) < sum(b):
    exit(print(-1))

for i in range(n):
    c[i] = a[i]-b[i]
c.sort()
minus = 0
cnt = 0
for i in range(n):
    if c[i] < 0:
        minus += c[i]
        cnt += 1
    else:
        break
if c[0] >= 0:
    print(0)
    exit()
for i in range(n):
    minus += c[-1-i]
    if minus >= 0:
        print(i+cnt+1)
        break