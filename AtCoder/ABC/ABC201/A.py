#n = int(input())
#x, y, z = map(int,input().split())
a = list(map(int,input().split()))
ans = cnt = 0
a.sort()
if (a[1] - a[0]) == (a[2] - a[1]):
    print("Yes")
else:
    print("No")