n = int(input())
l = list(map(int,input().split()))
l.sort()
sum = 0
for i in range(n-1):
    sum += l[i]
if (sum <= l[n-1]):
    print("No")
else:
    print("Yes")