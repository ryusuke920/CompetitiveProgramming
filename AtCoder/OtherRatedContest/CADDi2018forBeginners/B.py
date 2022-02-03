n,h,w = map(int,input().split())
cnt = 0
for i in range(n):
    a,b = map(int,input().split())
    if a >= h and b >= w:
        cnt += 1
print(cnt)