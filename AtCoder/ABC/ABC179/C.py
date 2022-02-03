n = int(input())
ans = 0
cnt = 0
for i in range(1,n):
    a = i
    if n%a == 0:
        b = n//a - 1
    else:
        b = n//a
    cnt += b
print(cnt)