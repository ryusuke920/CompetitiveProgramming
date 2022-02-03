n = int(input())
a = list(map(int,input().split()))
ch = [0]*2
i = 0
j = 2
ans = 1
a.sort()
a = a[::-1]
while True:
    if a[i] == a[i+1]:
        ch[0] = a[i]
        break
    else:
        i += 1
    if i == n-1:
        ans = 0
        break

while True:
    if ans == 0:
        break
    if a[i+j] == a[i+j+1]:
        ch[1] = a[i+j]
        break
    else:
        j += 1
    if i+j == n-1:
        ans = 0

if ans == 0:
    print(0)
else:
    print(ch[0]*ch[1])