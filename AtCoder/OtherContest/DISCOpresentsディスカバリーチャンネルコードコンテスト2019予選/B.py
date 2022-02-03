n = int(input())
ans = 0
if n%2 == 0:
    for i in range(2,n,2):
        ans += i
    print(ans*2)
else:
    for i in range(1,n,2):
        ans += i
    print(ans*2 - (n - 2))