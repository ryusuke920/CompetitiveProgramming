n = int(input())
ans = 0
for i in range(2,n):
    cnt = 0
    for j in range(2,int(i**0.5)+1):
        if i%j == 0:
            cnt += 1
    if cnt == 0:
        ans += 1
print(ans)