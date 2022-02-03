a,b,c = map(int,input().split())
k = int(input())
cnt = 0
while a >= b:
    cnt += 1
    b *= 2
while b >= c:
    cnt += 1
    c *= 2

if cnt <= k:
    print("Yes")
else:
    print("No")