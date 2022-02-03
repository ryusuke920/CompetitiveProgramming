n,t = map(int,input().split())
a = [0]*n
b = [0]*n
sa = [0]*n
for i in range(n):
    a[i], b[i] = map(int,input().split())
    sa[i] = a[i] - b[i]

out = sum(b)
if out > t:
    exit(print(-1))

cnt = 0
sa.sort(reverse = True)
num = sum(a)
if num <= t:
    print(0)
else:
    while True:
        num -= sa[cnt]
        cnt += 1
        if num <= t:
            print(cnt)
            break