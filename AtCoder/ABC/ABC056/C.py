x = int(input())
ans = 0
i = 1
while True:
    ans += i
    i += 1
    if ans >= x:
        print(i-1)
        break