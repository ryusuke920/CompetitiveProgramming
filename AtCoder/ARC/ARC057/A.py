a,k = map(int,input().split())
ans = a
count = 0
if k == 0:
    count = 2*(10**12) - a
else:
    while True:
        ans += ans*k + 1
        count += 1
        if ans >= 2*(10**12):
            break
print(count)