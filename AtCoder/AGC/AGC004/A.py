a = list(map(int,input().split()))
cnt = 0
for i in range(3):
    if a[i]%2 == 0:
        cnt += 1
if cnt == 0:
    a.sort()
    print(a[0]*a[1])
else:
    print(0)