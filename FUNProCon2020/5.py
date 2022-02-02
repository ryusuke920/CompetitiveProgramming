x,y = map(int,input().split())
for i in range(1, min(x + 1, y + 1)):
    if i == 1:
        ans = 1
    else:
        ans *= i
        ans %= y
print(ans%y)