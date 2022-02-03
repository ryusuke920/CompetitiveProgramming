a = []
for i in range(3):
    a += list(map(int, input().split()))
n = int(input())
for _ in range(n):
    b = int(input())
    if b in a:
        i = a.index(b)
        a[i] = 0
if sum(a[0:3]) == 0 or sum(a[3:6]) == 0 or sum(a[6:]) == 0 \
    or sum(a[0::3]) == 0 or sum(a[1::3]) == 0 or sum(a[2::3]) == 0 \
    or sum(a[0::4]) == 0 or sum(a[2:7:2]) == 0:
    print("Yes")
else:
    print("No")