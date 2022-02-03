n,a,b = map(int,input().split())
ans = 0
count = 0
for i in range(1,n+1):
    ch = i
    while True:
        ans += i%10
        if i == 0:
            if ans >= a and ans <= b:
                count += ch
            ans = 0
            break
        i //= 10
print(count)