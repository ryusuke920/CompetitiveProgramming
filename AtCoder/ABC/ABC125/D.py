n = int(input())
a = list(map(int,input().split()))
num = 0
mi = 10**9
for i in range(n):
    num += abs(a[i])
    if abs(mi) >= abs(a[i]):
        mi = a[i]
cnt = 0
for i in range(n):
    if a[i] < 0:
        cnt += 1
if cnt%2 == 1:
    print(num-2*abs(mi))
else:
    print(num)