n = int(input())
a = list(map(int,input().split()))
count = 0
for i in range(n):
    if a[i]%2 == 1:
        count += 1
if count%2 == 1:
    print("NO")
else:
    print("YES")