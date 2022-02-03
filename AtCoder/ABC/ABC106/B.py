n = int(input())
count = 0
ans = 0
for i in range(3,n+1,2):
    for j in range(1,i+2,2):
        if i%j == 0:
            count += 1
    if count == 8:
        ans += 1
        count = 0
    else:
        count = 0
print(ans)