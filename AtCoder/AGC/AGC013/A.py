n = int(input())
a = list(map(int,input().split()))
ans = 0
ch = 0
for i in range(n-1):
    if ch == 0 and a[i] < a[i+1]:
        ch = 1
    elif ch == 0 and a[i] > a[i+1]:
        ch = -1
    elif ch == 1 and a[i] > a[i+1]:
        ans += 1
        ch = 0
    elif ch == -1 and a[i] < a[i+1]:
        ans += 1
        ch = 0
print(ans+1)