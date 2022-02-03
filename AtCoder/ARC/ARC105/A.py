#n = int(input())
#a,b,c,d = map(int,input().split())
a = list(map(int,input().split()))
ans = 0
cnt = 0
if (a[0]+a[1] == a[2]+a[3]) or (a[0]+a[2] == a[1]+a[3]) or (a[0]+a[3] == a[2]+a[1]) or (a[0] == a[1] + a[2]+a[3]) or  (a[1] == a[0] + a[2]+a[3]) or  (a[2] == a[1] + a[0]+a[3]) or  (a[3] == a[1] + a[2]+a[0]):
    print("Yes")
else:
    print("No") 