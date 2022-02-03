n = int(input())
a = list(map(int,input().split()))
ch = 0 # increase -> 1, decrease -> 2
ans = 0
for i in range(n-1):
    if a[i] == a[i+1]: continue
    if ch == 0 and a[i] < a[i+1]:
        ch = 1
    elif ch == 0 and a[i] > a[i+1]:
        ch = 2
    elif ch == 1 and a[i] > a[i+1]:
        ans += 1
        ch = 0
    elif ch == 2 and a[i] < a[i+1]:
        ans += 1
        ch = 0

print(ans + 1)