n = int(input())
cnt = 0
for i in range(n):
    a,b = map(int,input().split())
    a += cnt
    print(i,a,b,cnt)
    if a%b != 0:
        if a >= b:
            cnt += a%b
        else:
            cnt += b-a
print(cnt)