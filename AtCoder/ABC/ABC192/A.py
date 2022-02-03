n = int(input())
ans = cnt = 0
while n % 100 != 0:
    ans += 1
    n += 1
if ans == 0:
    print(100)
else:
    print(ans)