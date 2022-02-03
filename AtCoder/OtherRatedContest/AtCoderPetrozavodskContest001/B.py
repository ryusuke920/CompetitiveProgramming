n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
ans = 0
for i in range(n):
    if a[i] == b[i]: continue
    elif a[i] > b[i]:
        ans += a[i] - b[i]
    else:
        ans += (b[i] - a[i])//2
if ans <= sum(b) - sum(a):
    print("Yes")
else:
    print("No")