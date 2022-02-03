n = int(input())
a = list(map(int,input().split()))
ans = 0
if n == 4 or n == 6:
    exit(print("No"))
for i in range(n):
    ans ^= a[i]
if ans == 0:
    print("Yes")
else:
    print("No")